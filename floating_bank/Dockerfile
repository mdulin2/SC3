FROM ubuntu:16.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim gdb gcc python git curl bsdmainutils nano tmux perl tcpdump -y

# Setup the users
## Setup the 'firsty' user 
RUN useradd -d /home/bank/ -m -p bank -s /bin/bash bank
RUN echo "bank:bank" | chpasswd
RUN chown -R root:bank  /home/bank

# Copy in the files
ADD bank.c /home/bank/bank.c

# Compile the code for this challenge
RUN gcc /home/bank/bank.c -o /home/bank/bank -O0 -ggdb -no-pie

ADD ./flag.txt /home/bank/flag.txt

# Setup the proper file for each set of exercises
RUN chown root:bank /home/bank/bank
RUN chown root:bank /home/bank/flag.txt
RUN chmod 4755 /home/bank/bank
RUN chmod 400 /home/bank/flag.txt
RUN chmod 744 /home/bank/bank.c

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d

