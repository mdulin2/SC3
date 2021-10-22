FROM ubuntu:16.04

WORKDIR /astros
RUN apt-get update && apt-get -y install build-essential gcc socat netcat
COPY ./signs ./signs
ENTRYPOINT socat TCP-LISTEN:10002,reuseaddr,fork EXEC:"/astros/signs",pty,stderr
