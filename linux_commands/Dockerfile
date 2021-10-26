FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim python git bsdmainutils nano -y

# Setup the users
## Setup the 'first_ssh' user 
RUN useradd -d /home/first_ssh/ -m -p first_ssh -s /bin/bash first_ssh
RUN echo "first_ssh:first_ssh" | chpasswd
RUN chown -R root:first_ssh  /home/first_ssh

## Setup the 'deeper' user 
RUN useradd -d /home/deeper/ -m -p deeper -s /bin/bash deeper
RUN echo "deeper:deeper" | chpasswd
RUN chown -R root:deeper  /home/deeper

## Setup the 'processes' user 
RUN useradd -d /home/processes/ -m -p processes -s /bin/bash processes
RUN echo "processes:processes" | chpasswd
RUN chown -R root:processes  /home/processes

ADD ./flag1.txt /home/first_ssh/flag.txt
# Create directory to add flag to
RUN mkdir /home/deeper/directory1/ 
ADD ./flag2.txt /home/deeper/directory1/flag.txt

ADD ./flag3.txt /home/processes/flag.txt
ADD ./ps_fun.sh /home/processes/ps_fun.sh

# Setup the proper file for each set of exercises
RUN chown root:first_ssh /home/first_ssh/flag.txt
RUN chmod 440 /home/first_ssh/flag.txt

# Setup the proper file for each set of exercises
RUN chown root:first_ssh /home/deeper/directory1/flag.txt
RUN chmod 440 /home/deeper/directory1/flag.txt

# Setup the proper file for each set of exercises
RUN chown root:first_ssh /home/processes/flag.txt
RUN chmod 400 /home/processes/flag.txt
RUN chown root:first_ssh /home/processes/ps_fun.sh
RUN chmod 550 /home/processes/ps_fun.sh

ADD ./start.sh /start.sh 

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT /start.sh

