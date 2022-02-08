#!/bin/bash 

/home/processes/ps_fun.sh `cat /home/processes/flag.txt` &
service ssh restart && sleep 5d