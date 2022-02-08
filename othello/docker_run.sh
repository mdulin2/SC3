#!/bin/bash 

sudo docker build . --tag othello
sudo docker run --privileged -d -p 10005:10005 -it othello

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
