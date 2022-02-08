#!/bin/bash 

sudo docker build . --tag post_delete
sudo docker run -d -p 8084:8084 -it post_delete

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
