#!/bin/bash 

sudo docker build . --tag patch 
sudo docker run --privileged -d -p 10004:10004 -it patch

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
