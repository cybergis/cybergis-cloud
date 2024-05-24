# TODO: Move most AWS-related endpoints with pure JavaScript on website frontend.

import asyncio
import boto3
from datetime import datetime
from quart import make_response, Quart, request, websocket
from quart_cors import cors
from json import loads
from random import choices
from string import ascii_letters, digits
from threading import Thread


app = Quart(__name__)
app = cors(app)


cache = {}


def generate_identifier() -> str:
    return "".join(choices(ascii_letters + digits, k=6)) + datetime.now().strftime("%m%d%H%M%S")


def create_session(access_key: str, secret_access_key: str, region: str) -> boto3.Session:
    """
    Create boto3 session with user account.
    """
    try:
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_access_key,
            region_name=region
        )
    except Exception as error:
        raise Exception("Unexpected error: Failed to create session with provided credentials.")

    return session


def create_cluster_stack(availability_zone: str, session: boto3.Session, cluster_stack_name: str, head_node_instance_type: str, head_node_start_script_url: str, compute_node_instance_type: str, compute_node_count: int, compute_node_configured_script_url: str, shared_storage_size: int):
    """
    Create cluster CloudFormation stack on user account.
    """
    cloudformation_client = session.client("cloudformation")

    try:
        with open("compiled_templates/cluster.yaml", "r") as file:
            cluster_template = file.read()
    except Exception as error:
        raise Exception("Unexpected Error: Failed to read cluster.yaml.")

    create_stack_response = cloudformation_client.create_stack(
        StackName=cluster_stack_name,
        TemplateBody=cluster_template,
        Parameters=[
            {
                "ParameterKey": "AvailabilityZone",
                "ParameterValue": availability_zone
            },
            {
                "ParameterKey": "HeadNodeInstanceType",
                "ParameterValue": head_node_instance_type
            },
            {
                "ParameterKey": "HeadNodeOnStartScriptURL",
                "ParameterValue": head_node_start_script_url
            },
            {
                "ParameterKey": "ComputeNodeInstanceType",
                "ParameterValue": compute_node_instance_type
            },
            {
                "ParameterKey": "ComputeNodeCount",
                "ParameterValue": str(compute_node_count)
            },
            {
                "ParameterKey": "ComputeNodeOnConfiguredScriptURL",
                "ParameterValue": compute_node_configured_script_url
            },
            {
                "ParameterKey": "SharedStorageSize",
                "ParameterValue": str(shared_storage_size)
            }
        ],
        Capabilities=[
            "CAPABILITY_NAMED_IAM",
            "CAPABILITY_AUTO_EXPAND"
        ],
        OnFailure="DELETE"
    )


def find_cluster_instance_type(access_key: str, secret_access_key: str, region: str, vcpus: int, ram: float, gpus: int, vram: float):
    """
    Find optimal EC2 instance type for user configuration.
    TODO: Give user multiple instance type options / offer more specific configuration details.
    TODO: Do some cleanup here.
    """
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
                    {
                        "Field": "marketoption",
                        "Type": "TERM_MATCH",
                        "Value": "OnDemand"
                    }
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
                        {
                            "Field": "marketoption",
                            "Type": "TERM_MATCH",
                            "Value": "OnDemand"
                        }
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

    # TODO: Handle ties better.
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

    return smallest_cost, instance_type


def submit_task(access_key, secret_access_key, region, availability_zone, identifier, cluster_slave_vcpu_amount, cluster_slave_ram_amount, cluster_slave_instance_count):
    """
    Asynchronously handle user cluster creation request.
    """
    _, cluster_slave_instance_type = find_cluster_instance_type(access_key, secret_access_key, region, cluster_slave_vcpu_amount, cluster_slave_ram_amount, 0, 0)
    
    session = create_session(access_key, secret_access_key, region)

    cluster_stack_name = "cybergis-" + identifier

    create_cluster_stack(availability_zone, session, cluster_stack_name, "t3.medium", "https://raw.githubusercontent.com/cybergis/cybergis-cloud/main/scripts/head_start.sh", cluster_slave_instance_type, cluster_slave_instance_count, "https://raw.githubusercontent.com/cybergis/cybergis-cloud/main/scripts/slave_configured.sh", 64)


def get_status(access_key, secret_access_key, region, stack_name):
    session = create_session(access_key, secret_access_key, region)

    cloudformation_client = session.client("cloudformation")

    try:
        try:
            describe_stack_instance_response = cloudformation_client.describe_stacks(
                StackName=stack_name
            )
            cluster_status = describe_stack_instance_response["Stacks"][0]["StackStatus"]
            return cluster_status
        except Exception as error:
            pass
    except Exception as error:
        pass

    return "COULD_NOT_OBTAIN"


def rename_status(stack_status):
    if stack_status == "CREATE_IN_PROGRESS":
        return "creation in progress"
    elif stack_status == "CREATE_FAILED":
        return "creation failed"
    elif stack_status == "CREATE_COMPLETE":
        return "created successfully"
    elif stack_status == "ROLLBACK_IN_PROGRESS":
        return "failed to create and is rolling back"
    elif stack_status == "ROLLBACK_FAILED":
        return "failed to rollback"
    elif stack_status == "ROLLBACK_COMPLETE":
        return "rolled back successfully"
    elif stack_status == "DELETE_IN_PROGRESS":
        return "deletion in progress"
    elif stack_status == "DELETE_FAILED":
        return "deletion failed"
    elif stack_status == "DELETE_COMPLETE":
        return "deleted successfully"
    elif stack_status == "COULD_NOT_OBTAIN":
        return "status could not be obtained"
    else:
        return "has unknown status"


@app.route("/submit", methods=["POST"])
async def submit():
    """
    Respond to user cluster creation request.
    """
    identifier = generate_identifier()

    form = await request.form

    access_key = form["access-key"]
    secret_access_key = form["secret-access-key"]

    region = form["region"]
    availability_zone = region + form["availability-zone"]

    cluster_slave_vcpu_amount = int(form["cluster-slave-vcpu-amount"])
    cluster_slave_ram_amount = float(form["cluster-slave-ram-amount"])
    cluster_slave_instance_count = int(form["cluster-slave-instance-count"])

    # Asynchronously handle submissions for quick web response time.
    task = Thread(target=submit_task, kwargs={"access_key": access_key, "secret_access_key": secret_access_key, "region": region, "availability_zone": availability_zone, "identifier": identifier, "cluster_slave_vcpu_amount": cluster_slave_vcpu_amount, "cluster_slave_ram_amount": cluster_slave_ram_amount, "cluster_slave_instance_count": cluster_slave_instance_count})
    task.start()  # TODO: Validate if best practice.

    cache_status = {
        "main": "not started",
        "provider": "not started",
        "cluster": "not started",
        "compute_fleet": "not started",
        "url": "n/a",
        "delete": False
    }
    cache[identifier] = {"access_key": access_key, "secret_access_key": secret_access_key, "region": region, "status": cache_status}

    return await make_response(f"Token: {identifier}")


@app.route("/status", methods=["POST"])
async def status():
    """
    Get status of cluster creation on user account.
    """
    cluster_status = "COULD NOT OBTAIN"

    form = await request.form

    identifier = form["identifier"]
    if identifier in cache:
        access_key = cache[identifier]["access_key"]
        secret_access_key = cache[identifier]["secret_access_key"]
        region = cache[identifier]["region"]

        cluster_name = "c-cybergis-" + identifier

        session = create_session(access_key, secret_access_key, region)

        cloudformation_client = session.client("cloudformation")

        try:
            try:
                describe_stack_instance_response = cloudformation_client.describe_stacks(
                    StackName=cluster_name
                )
                cluster_status = describe_stack_instance_response["Stacks"][0]["StackStatus"].replace("_", " ")
                if cluster_status == "CREATE COMPLETE":
                    describe_stack_resource_response = cloudformation_client.describe_stack_resource(
                        StackName=cluster_name,
                        LogicalResourceId="HeadNode"
                    )
                    head_node_id = describe_stack_resource_response["StackResourceDetail"]["PhysicalResourceId"]
                    ec2_resource = session.resource("ec2")
                    public_dns_name = ec2_resource.Instance(head_node_id).public_dns_name
                    if public_dns_name[0:3] != "ec2" or public_dns_name[-len("amazonaws.com"):] != "amazonaws.com":
                        raise Exception("Unexpected error: Failed to obtain public DNS name of created head node.")
                    cluster_status += f" (http://{public_dns_name}:8888)"
            except Exception as error:
                pass
        except Exception as error:
            pass
    else:
        return await make_response("<p>Invalid token.</p>")

    return await make_response(f"<p>Cluster Status: {cluster_status}</p>")


@app.websocket("/status/<identifier>")
async def status_ws(identifier):
    """
    Get status of cluster creation on user account.
    """

    while True:
        if identifier in cache:
            access_key = cache[identifier]["access_key"]
            secret_access_key = cache[identifier]["secret_access_key"]
            region = cache[identifier]["region"]

            session = create_session(access_key, secret_access_key, region)
            cloudformation_resource = session.resource("cloudformation")

            main_name = f"cybergis-{identifier}"
            provider_name = f"cybergis-{identifier}-ParallelClusterProvider-"
            cluster_name = f"c-cybergis-{identifier}"
            compute_fleet_name = f"c-cybergis-{identifier}-ComputeFleetQueuesNestedStackQueuesNestedStackResource"
            stacks = [stack.name for stack in cloudformation_resource.stacks.all()]
            # TODO: Do some minor optimization/cleanup here.
            for stack in stacks:
                if stack.startswith(provider_name):
                    provider_name = stack
                    break
            for stack in stacks:
                if stack.startswith(compute_fleet_name):
                    compute_fleet_name = stack
                    break

            main_status = rename_status(get_status(access_key, secret_access_key, region, main_name))
            if main_status == "status could not be obtained" and cache[identifier]["status"]["main"] == "not started" and cache[identifier]["status"]["delete"] == False:
                main_status = "not started"
            elif main_status == "status could not be obtained" and cache[identifier]["status"]["delete"] == True:
                main_status = "deleted successfully"
            if "delet" in main_status or ("roll" in main_status and "back" in main_status):
                cache[identifier]["status"]["delete"] = True
            if main_status != cache[identifier]["status"]["main"]:
                cache[identifier]["status"]["main"] = main_status
                await websocket.send(f"Main stack {main_status}.")
                if main_status == "deleted successfully":
                    await websocket.close(1000)
                    break

            provider_status = rename_status(get_status(access_key, secret_access_key, region, provider_name))
            if provider_status == "status could not be obtained" and cache[identifier]["status"]["provider"] == "not started" and cache[identifier]["status"]["delete"] == False:
                provider_status = "not started"
            elif provider_status == "status could not be obtained" and cache[identifier]["status"]["delete"] == True:
                provider_status = "deleted successfully"
            if "delet" in provider_status or ("roll" in provider_status and "back" in provider_status):
                cache[identifier]["status"]["delete"] = True
            if provider_status != cache[identifier]["status"]["provider"]:
                cache[identifier]["status"]["provider"] = provider_status
                await websocket.send(f"Provider stack {provider_status}.")

            cluster_status = rename_status(get_status(access_key, secret_access_key, region, cluster_name))
            if cluster_status == "status could not be obtained" and cache[identifier]["status"]["cluster"] == "not started" and cache[identifier]["status"]["delete"] == False:
                cluster_status = "not started"
            elif cluster_status == "status could not be obtained" and cache[identifier]["status"]["delete"] == True:
                cluster_status = "deleted successfully"
            if "delet" in cluster_status or ("roll" in cluster_status and "back" in cluster_status):
                cache[identifier]["status"]["delete"] = True
            if cluster_status != cache[identifier]["status"]["cluster"]:
                cache[identifier]["status"]["cluster"] = cluster_status
                await websocket.send(f"Cluster stack {cluster_status}.")
            if cluster_status == "created successfully" and cache[identifier]["status"]["url"] == "n/a":
                cloudformation_client = session.client("cloudformation")
                try:
                    describe_stack_resource_response = cloudformation_client.describe_stack_resource(
                        StackName=cluster_name,
                        LogicalResourceId="HeadNode"
                    )
                    head_node_id = describe_stack_resource_response["StackResourceDetail"]["PhysicalResourceId"]
                    ec2_resource = session.resource("ec2")
                    public_dns_name = ec2_resource.Instance(head_node_id).public_dns_name
                    if public_dns_name[0:3] != "ec2" or public_dns_name[-len("amazonaws.com"):] != "amazonaws.com":
                        raise Exception("Unexpected error: Failed to obtain public DNS name of created head node.")
                    notebook_url = f"http://{public_dns_name}:8888"
                    cache[identifier]["status"]["url"] = notebook_url
                    await websocket.send(f"Notebook URL is {notebook_url}.")
                except Exception as error:
                    pass

            compute_fleet_status = rename_status(get_status(access_key, secret_access_key, region, compute_fleet_name))
            if compute_fleet_status == "status could not be obtained" and cache[identifier]["status"]["compute_fleet"] == "not started" and cache[identifier]["status"]["delete"] == False:
                compute_fleet_status = "not started"
            elif compute_fleet_status == "status could not be obtained" and cache[identifier]["status"]["delete"] == True:
                compute_fleet_status = "deleted successfully"
            if "delet" in compute_fleet_status or ("roll" in compute_fleet_status and "back" in compute_fleet_status):
                cache[identifier]["status"]["delete"] = True
            if compute_fleet_status != cache[identifier]["status"]["compute_fleet"]:
                cache[identifier]["status"]["compute_fleet"] = compute_fleet_status
                await websocket.send(f"Compute fleet stack {compute_fleet_status}.")

        else:
            await websocket.send(f"User token is invalid.")
            await websocket.close(1000)
            break

        await asyncio.sleep(15)


@app.route("/delete", methods=["POST"])
async def delete():
    """
    Delete a cluster on user account.
    """
    form = await request.form

    identifier = form["identifier"]

    if identifier in cache:
        access_key = cache[identifier]["access_key"]
        secret_access_key = cache[identifier]["secret_access_key"]
        region = cache[identifier]["region"]

        cluster_stack_name = "cybergis-" + identifier

        session = create_session(access_key, secret_access_key, region)

        cloudformation_client = session.client("cloudformation")
        try:
            delete_stack_response = cloudformation_client.delete_stack(
                StackName=cluster_stack_name
            )
            cache[identifier]["status"]["delete"] = True
        except Exception as error:
            pass

    else:
        return await make_response("<p>Invalid token.</p>")

    return await make_response("<p>Delete request sent. Check status.</p>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=500, ssl_context=("midware.crt", "midware.key"))
