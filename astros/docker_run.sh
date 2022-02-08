#!/bin/bash 

sudo docker build . --tag astros
sudo docker run -d -p 10002:10002 -it astros

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
