FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim gdb gcc python git curl bsdmainutils nano tmux -y

# Setup the users
## Setup the 'firsty' user 
RUN useradd -d /home/signal/ -m -p signal -s /bin/bash signal
RUN echo "signal:signal" | chpasswd
RUN chown -R root:signal  /home/signal

# Copy in the files
ADD signal.c /home/signal/signal.c

# Compile the code for this challenge
RUN gcc /home/signal/signal.c -o /home/signal/signal -O0 -ggdb -no-pie

ADD ./flag.txt /home/signal/flag.txt

# Setup the proper file for each set of exercises
RUN chown root:signal /home/signal/signal
RUN chown root:signal /home/signal/flag.txt
RUN chmod 4755 /home/signal/signal
RUN chmod 400 /home/signal/flag.txt
RUN chmod 744 /home/signal/signal.c

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d

