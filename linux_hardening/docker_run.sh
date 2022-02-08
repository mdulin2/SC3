#!/bin/bash 

sudo docker build . --tag linux_hardening
sudo docker run -d -p 8090:80 -p 2121:21 -p 3000-3010:3000-3010  -it linux_hardening

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
