FROM ubuntu:18.04

RUN apt update -q &&\
    apt install -yq \
      python3-pip \
      git \
      ssh

RUN pip3 install awscli==1.16.229
WORKDIR /opt/integrations

COPY ./requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY ./ /opt/integrations/
