FROM ubuntu:16.04

WORKDIR /amazon-challenge
RUN apt-get update && apt-get -y install build-essential gcc socat netcat
CMD gcc -o amazon amazon.c
ENTRYPOINT socat TCP-LISTEN:10001,reuseaddr,fork EXEC:"/amazon-challenge/amazon",pty,stderr
