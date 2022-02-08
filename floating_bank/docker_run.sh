#!/bin/bash 

sudo docker build . --floating_bank
sudo docker run -d -p 2224:22 --cap-add=SYS_PTRACE -it floating_bank

# DEBUG version -- goes into the container automatically
docker_ps=$(sudo docker ps -q | head -n1) 
sudo docker exec -u root -it $docker_ps /bin/bash
