FROM ubuntu:20.04

WORKDIR /application
RUN apt-get update && apt-get -y install build-essential python3 python3-pip tmux
RUN pip3 install Flask flask-cors requests

COPY ./backend ./backend
COPY ./frontend ./frontend

WORKDIR /
COPY ./flag_host ./flag_host
COPY ./flag.txt ./flag.txt

# Start everything up!
COPY ./start.sh start.sh
CMD ./start.sh
