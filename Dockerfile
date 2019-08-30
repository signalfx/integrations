FROM ubuntu:18.04

RUN apt update -q &&\
    apt install -yq \
      python3-pip

RUN pip3 install awscli==1.16.229
WORKDIR /opt/integrations

COPY ./ /opt/integrations/
