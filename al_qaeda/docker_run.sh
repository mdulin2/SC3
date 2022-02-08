#!/bin/bash 

# Use the pre-built lamp stack with our pre-populated database to run this
sudo docker run -i -t -p "80:80" -v ${PWD}/src/app:/app -v ${PWD}/src/mysql:/var/lib/mysql mattrayner/lamp:latest-1804

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
