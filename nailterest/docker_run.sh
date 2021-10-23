#!/bin/bash 

sudo docker build . --tag nailterest
sudo docker run -d -p 8080:8080 -p 8081:8081 -it nailterest

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
