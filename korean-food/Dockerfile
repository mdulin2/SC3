FROM ubuntu:20.04

WORKDIR /application
RUN apt-get update 

RUN DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt-get -y install build-essential nodejs npm tmux mysql-server
RUN npm install --global yarn
RUN apt-get install -y vim

# Copy over the bulk of the code base
COPY ./react-backend ./react-backend
COPY ./client ./client
COPY ./flag.txt ./flag.txt

# Install packages for both frontend and backend
WORKDIR /application/react-backend
RUN npm install
WORKDIR /application/client 
RUN yarn 

# Start everything up!
COPY ./start.sh start.sh
CMD ./start.sh

#ENTRYPOINT /bin/bash