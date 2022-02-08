#!/bin/bash 

sudo docker build . --tag lebean
sudo docker run -d -p 8083:8083 -it lebean

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
