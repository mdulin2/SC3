#!/bin/bash 

sudo docker build . --tag korean_food
sudo docker run --privileged -d -p 8085:8085 -p 8081:8081 -it korean_food

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
