import asyncio
from json import loads
from random import choices
from threading import Thread

import boto3
from dataclasses import dataclass
from datetime import datetime
from flask import Flask, request, jsonify
from pathlib import Path
import pcluster.lib as pc
from string import ascii_letters, digits

import os

import nest_asyncio
nest_asyncio.apply()


app = Flask(__name__)


cache = {}


def generate_identifier() -> str:
    return "".join(choices(ascii_letters + digits, k=8)) + "-" + datetime.now().strftime("%Y%m%d%H%M%S")


def create_session(access_key: str, secret_access_key: str, region: str) -> boto3.Session:
    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_access_key,
            region_name=region
        )
    except Exception as error:
        raise Exception("Unexpected error: Failed to create session with provided credentials.")

    return session


def create_network(availability_zone: str, session: boto3.Session, network_stack_name: str, file_system_name: str):
    cloudformation_client = session.client("cloudformation")

    try:
        with open("compiled_templates/network.yaml", "r") as file:
            network_template = file.read()
    except Exception as error:
        raise Exception("Unexpected Error: Failed to read network.yaml.")

    create_stack_response = cloudformation_client.create_stack(
        StackName=network_stack_name,
        TemplateBody=network_template,
        Parameters=[
            {
                "ParameterKey": "FileSystemName",
                "ParameterValue": file_system_name
            },
            {
                "ParameterKey": "AvailabilityZone",
                "ParameterValue": availability_zone
            }
        ]
    )

    return


def get_network_details(session: boto3.Session, network_stack_name: str) -> (str, str, str):
    while True:
        cloudformation_client = session.client("cloudformation")
        try:
            describe_stack_instance_response = cloudformation_client.describe_stacks(
                StackName=network_stack_name
            )
            if describe_stack_instance_response["Stacks"][0]["StackStatus"] == "CREATE_COMPLETE":
                outputs = describe_stack_instance_response["Stacks"][0]["Outputs"]
                for output in outputs:
                    if "PublicSubnetId" == output["OutputKey"]:
                        public_subnet_id = output["OutputValue"]
                    elif "DefaultSecurityGroup" == output["OutputKey"]:
                        default_security_group = output["OutputValue"]
                    elif "FileSystemId" == output["OutputKey"]:
                        file_system_id = output["OutputValue"]
                break
            elif describe_stack_instance_response["Stacks"][0]["StackStatus"] == "CREATE_IN_PROGRESS":
                pass
            else:
                raise Exception("Unexpected error: Network stack status was not recognized.")
        except Exception as error:
            raise Exception("Unexpected error: Network stack status could not be obtained.")

    return (public_subnet_id, default_security_group, file_system_id)


def find_cluster_instance_type(access_key: str, secret_access_key: str, region: str, vcpus: int, ram: float, gpus: int, vram: float):
    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_access_key,
            region_name="us-east-1"
        )
    except Exception as error:
        raise Exception("Unexpected error: Failed to create session with provided credentials.")

    instance_types = None
    valid_cluster_instances = None
    cluster_products = None

    if instance_types is None:
        if valid_cluster_instances is None:
            valid_cluster_instances = []
            ec2_client = session.client("ec2")
            valid_cluster_products = []
            describe_instance_types_response = ec2_client.describe_instance_types(
                Filters=[
                    {
                        "Name": "processor-info.supported-architecture",
                        "Values": [
                            "x86_64"
                        ]
                    }
                ]
            )
            valid_cluster_products += describe_instance_types_response["InstanceTypes"]
            if "NextToken" not in describe_instance_types_response:
                next_token = "null"
            else:
                next_token = describe_instance_types_response["NextToken"]
            while next_token != "null":
                describe_instance_types_response = ec2_client.describe_instance_types(
                    Filters=[
                        {
                            "Name": "processor-info.supported-architecture",
                            "Values": [
                                "x86_64"
                            ]
                        }
                    ],
                    NextToken=next_token
                )
                valid_cluster_products += describe_instance_types_response["InstanceTypes"]
                if "NextToken" not in describe_instance_types_response:
                    next_token = "null"
                else:
                    next_token = describe_instance_types_response["NextToken"]
            for product in valid_cluster_products:
                valid_cluster_instances.append(product["InstanceType"])

        instance_types = {}

        if cluster_products is None:
            cluster_products = []
            pricing_client = session.client("pricing")
            products_response = pricing_client.get_products(
                ServiceCode="AmazonEC2",
                Filters=[
                    {
                        "Field": "productFamily",
                        "Type": "TERM_MATCH",
                        "Value": "Compute Instance",
                    },
                    {
                        "Field": "regionCode",
                        "Type": "TERM_MATCH",
                        "Value": region,
                    },
                    {
                        "Field": "operatingSystem",
                        "Type": "TERM_MATCH",
                        "Value": "Linux"
                    },
                    {
                        "Field": "tenancy",
                        "Type": "TERM_MATCH",
                        "Value": "shared"
                    },
                    {
                        "Field": "capacitystatus",
                        "Type": "TERM_MATCH",
                        "Value": "Used"
                    },
                    {
                        "Field": "preInstalledSw",
                        "Type": "TERM_MATCH",
                        "Value": "NA"
                    },
                    {
                        "Field": "processorArchitecture",
                        "Type": "TERM_MATCH",
                        "Value": "64-bit"
                    },
                ]
            )
            cluster_products += products_response["PriceList"]
            while "NextToken" in products_response:
                products_response = pricing_client.get_products(
                    ServiceCode="AmazonEC2",
                    Filters=[
                        {
                            "Field": "productFamily",
                            "Type": "TERM_MATCH",
                            "Value": "Compute Instance",
                        },
                        {
                            "Field": "regionCode",
                            "Type": "TERM_MATCH",
                            "Value": region,
                        },
                        {
                            "Field": "operatingSystem",
                            "Type": "TERM_MATCH",
                            "Value": "Linux"
                        },
                        {
                            "Field": "tenancy",
                            "Type": "TERM_MATCH",
                            "Value": "shared"
                        },
                        {
                            "Field": "capacitystatus",
                            "Type": "TERM_MATCH",
                            "Value": "Used"
                        },
                        {
                            "Field": "preInstalledSw",
                            "Type": "TERM_MATCH",
                            "Value": "NA"
                        },
                        {
                            "Field": "processorArchitecture",
                            "Type": "TERM_MATCH",
                            "Value": "64-bit"
                        },
                    ],
                    NextToken=products_response["NextToken"]
                )
                cluster_products += products_response["PriceList"]

        for item in cluster_products:
            properties = loads(item)
            instance_name = properties["product"]["attributes"]["instanceType"]
            if instance_name not in valid_cluster_instances:
                continue
            memory = properties["product"]["attributes"]["memory"]
            vcpu = properties["product"]["attributes"]["vcpu"]
            if "gpuMemory" not in properties["product"]["attributes"]:
                gpu_memory = "0"
            else:
                gpu_memory = properties["product"]["attributes"]["gpuMemory"]
            if "gpu" not in properties["product"]["attributes"]:
                gpu = "0"
            else:
                gpu = properties["product"]["attributes"]["gpu"]
            network_performance = properties["product"]["attributes"]["networkPerformance"]
            # physical_gpu = properties["product"]["attributes"]["physicalGpu"]

            price = None
            for key1, value1 in properties["terms"]["OnDemand"].items():
                if len(properties["terms"]["OnDemand"].values()) != 1:
                    raise Exception("")
                for key2, value2 in value1["priceDimensions"].items():
                    if len(value1["priceDimensions"].values()) != 1:
                        raise Exception("")
                    if value2["unit"] == "Hrs":
                        price = value2["pricePerUnit"]["USD"]
            if price is None:
                raise Exception("Unexpected Error: Could not find price for a EC2 instance entry.")

            if "GB" in gpu_memory:
                gpu_memory = gpu_memory[0:gpu_memory.find("GB")-1]

            if gpu == "NA":
                gpu = 0

            if gpu_memory == "NA":
                gpu_memory = 0

            if "GiB" in memory:
                memory = memory[0:-4]
            elif "MiB" in memory:
                memory = float(memory[0:-4]) / 1024
            else:
                raise Exception("Unexpected Error: Could not determine size of memory of a EC2 instance entry.")

            instance = {
                "RAM": float(memory),
                "vCPU": float(vcpu),
                "VRAM": float(gpu_memory),
                "GPUs": float(gpu),
                "cost": float(price)
            }

            if instance_name in instance_types:
                raise Exception("Unexpected Error: Found duplicate notebook instance pricing entries.")
            instance_types[instance_name] = instance

    # TODO: handle ties better...
    smallest_cost_type = None
    smallest_cost = None
    for key, value in instance_types.items():
        if value["vCPU"] >= vcpus and value["RAM"] >= ram and value["GPUs"] >= gpus and value["VRAM"] >= vram:
            if smallest_cost is None:
                smallest_cost = value["cost"]
                smallest_cost_type = key
            elif smallest_cost > value["cost"]:
                smallest_cost = value["cost"]
                smallest_cost_type = key

    if smallest_cost_type is None:
        raise Exception("Unexpected Error: Could not find a sufficient slave instance type.")

    instance_type = smallest_cost_type

    print(smallest_cost)
    print(smallest_cost_type)

    return smallest_cost, instance_type


async def create_cluster(access_key: str, secret_access_key:str, region: str, session: boto3.Session, identifier: str, public_subnet_id: str, default_security_group: str, file_system_name: str, file_system_id: str, cluster_slave_instance_type: str, cluster_slave_instance_count: int):
    os.environ["AWS_ACCESS_KEY_ID"] = access_key
    os.environ["AWS_SECRET_ACCESS_KEY"] = secret_access_key

    try:
        with open("templates/cluster.txt", "r") as file:
            CLUSTER_TEMPLATE = file.read()
    except Exception as error:
        raise Exception("Unexpected Error: Failed to read cluster.txt.")

    ec2_client = session.client("ec2")
    KEY_NAME = "parallelclusterkeypair-" + identifier
    try:
        ec2_client.create_key_pair(
            KeyName=KEY_NAME
        )
    except:
        raise Exception("Unexpected error: Failed to create key pair for head node.")

    HEAD_NODE_PRIO1_SCRIPT_URL = "https://raw.githubusercontent.com/anuj-p/CyberGIS-cluster-scripts/main/head_init.sh"
    HEAD_NODE_PRIO2_SCRIPT_URL = "https://raw.githubusercontent.com/anuj-p/CyberGIS-cluster-scripts/main/head_start.sh"
    SLAVE_NODE_PRIO2_SCRIPT_URL = "https://raw.githubusercontent.com/anuj-p/CyberGIS-cluster-scripts/main/slave_init.sh"

    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{REGION}", region)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{OS}", "ubuntu2004")
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{HEAD_NODE_INSTANCE_TYPE}", "t3a.micro")
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{SUBNET_ID}", public_subnet_id)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{KEY_NAME}", KEY_NAME)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{HEAD_NODE_PRIO1_SCRIPT_URL}", HEAD_NODE_PRIO1_SCRIPT_URL)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{HEAD_NODE_PRIO2_SCRIPT_URL}", HEAD_NODE_PRIO2_SCRIPT_URL)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{SLAVE_NODE_INSTANCE_TYPE_NAME}", cluster_slave_instance_type.replace(".", ""))
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{SLAVE_NODE_INSTANCE_TYPE}", cluster_slave_instance_type)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{SLAVE_NODE_MIN_INSTANCE_COUNT}", str(cluster_slave_instance_count))
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{SLAVE_NODE_MAX_INSTANCE_COUNT}", str(cluster_slave_instance_count))
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{SLAVE_NODE_PRIO2_SCRIPT_URL}", SLAVE_NODE_PRIO2_SCRIPT_URL)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{FILE_SYSTEM_NAME}", file_system_name)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{FILE_SYSTEM_ID}", file_system_id)
    CLUSTER_TEMPLATE = CLUSTER_TEMPLATE.replace("{SECURITY_GROUP}", default_security_group)

    Path("compiled_templates").mkdir(exist_ok=True)
    try:
        with open("compiled_templates/cluster.yaml", "w") as file:
            file.write(CLUSTER_TEMPLATE)
    except Exception as e:
        raise Exception("Unexpected Error: Failed to write cluster template.")

    cluster_name = "parallelcluster-" + identifier
    pc.create_cluster(
        cluster_name=cluster_name,
        cluster_configuration="compiled_templates/cluster.yaml"
    )
    return


def submit_task(access_key, secret_access_key, region, availability_zone, identifier, cluster_slave_vcpu_amount, cluster_slave_ram_amount, cluster_slave_instance_count):
    _, cluster_slave_instance_type = find_cluster_instance_type(access_key, secret_access_key, region, cluster_slave_vcpu_amount, cluster_slave_ram_amount, 0, 0)

    session = create_session(access_key, secret_access_key, region)

    network_stack_name = "parallelclusternetworking-pub-" + identifier
    file_system_name = "pcfs-" + identifier
    create_network(availability_zone, session, network_stack_name, file_system_name)

    (public_subnet_id, default_security_group, file_system_id) = get_network_details(session, network_stack_name)

    # asyncio.set_event_loop(asyncio.SelectorEventLoop())
    asyncio.new_event_loop().run_until_complete(create_cluster(access_key, secret_access_key, region, session, identifier, public_subnet_id, default_security_group, file_system_name, file_system_id, cluster_slave_instance_type, cluster_slave_instance_count))


@app.route("/submit", methods=["POST"])
def submit():
    identifier = generate_identifier()

    print(request.form)

    access_key = request.form["access-key"]
    secret_access_key = request.form["secret-access-key"]

    region = request.form["region"]
    availability_zone = region + request.form["availability-zone"]

    # cluster_slave_instance_type = request.form["cluster-slave-instance-type"]
    cluster_slave_vcpu_amount = int(request.form["cluster-slave-vcpu-amount"])
    cluster_slave_ram_amount = float(request.form["cluster-slave-ram-amount"])
    cluster_slave_instance_count = int(request.form["cluster-slave-instance-count"])

    task = Thread(target=submit_task, kwargs={"access_key": access_key, "secret_access_key": secret_access_key, "region": region, "availability_zone": availability_zone, "identifier": identifier, "cluster_slave_vcpu_amount": cluster_slave_vcpu_amount, "cluster_slave_ram_amount": cluster_slave_ram_amount, "cluster_slave_instance_count": cluster_slave_instance_count})
    task.start()

    cache[identifier] = {"access_key": access_key, "secret_access_key": secret_access_key, "region": region}

    return f"Token: {identifier}", 200


@app.route("/status", methods=["POST"])
def status():
    print(request.form)

    network_status = "COULD NOT OBTAIN"
    cluster_status = "COULD NOT OBTAIN"

    identifier = request.form["identifier"]
    if identifier in cache:
        access_key = cache[identifier]["access_key"]
        secret_access_key = cache[identifier]["secret_access_key"]
        region = cache[identifier]["region"]

        network_stack_name = "parallelclusternetworking-pub-" + identifier
        cluster_name = "parallelcluster-" + identifier

        session = create_session(access_key, secret_access_key, region)

        cloudformation_client = session.client("cloudformation")
        try:
            describe_stack_instance_response = cloudformation_client.describe_stacks(
                StackName=network_stack_name
            )
            network_status = describe_stack_instance_response["Stacks"][0]["StackStatus"].replace("_", " ")
        except Exception as error:
            pass

        try:
            describe_stack_instance_response = cloudformation_client.describe_stacks(
                StackName=cluster_name
            )
            cluster_status = describe_stack_instance_response["Stacks"][0]["StackStatus"].replace("_", " ")
        except Exception as error:
            pass

    return f"<p>Network Status: {network_status}\n</p><p>Cluster Status: {cluster_status}</p>", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

