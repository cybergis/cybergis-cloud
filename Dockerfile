FROM ubuntu:22.04
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/00-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker
WORKDiR /root
EXPOSE 500
RUN DEBIAN_FRONTEND=noninteractive \
    apt update \
    && apt install -y python3 python3-pip git \
    && pip3 install boto3==1.24.18 quart==0.19.4 quart-cors==0.7.0 \
    && rm -rf /var/lib/apt/lists/*
