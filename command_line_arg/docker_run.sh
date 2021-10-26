#!/bin/bash 

sudo docker build . --tag hello_world
sudo docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -d -p 2226:22 -it hello_world 

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
