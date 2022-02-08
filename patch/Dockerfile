FROM ubuntu:16.04

WORKDIR /patch
RUN apt-get update && apt-get -y install build-essential python3 python3-pip
RUN pip3 install flask
COPY ./server.py ./server.py
COPY ./flag ./flag
COPY ./easy_auth ./easy_auth

# Add the 'patch' user
RUN useradd -d /home/patch/ -m -p patch -s /bin/bash patch

# Set the permissions of the files/directories
RUN chown -R root:patch  /patch /patch/* 
RUN chmod 555 ./server.py ./flag ./easy_auth

# Change the execution of the container to a different user
# We use a different user so that nothing can be deleted during execution
USER patch

## Run on port 10004
CMD ["python3","server.py"]
