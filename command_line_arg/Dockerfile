FROM ubuntu:20.04

RUN apt-get update -y && apt install openssh-server g++-multilib vim gdb -y

# Create ctf user
RUN useradd -d /home/hello_world/ -m -p hello_world -s /bin/bash hello_world
RUN echo "hello_world:hello_world" | chpasswd
WORKDIR /home/hello_world
RUN chown -R root:hello_world  /home/hello_world

# Copy in the files
ADD hello_world /home/hello_world/
ADD hello_world.c /home/hello_world/
ADD flag.txt /home/hello_world/

# Setup the proper file permissions
RUN chown root:hello_world /home/hello_world/hello_world
RUN chown root:hello_world /home/hello_world/flag.txt
RUN chmod 4755 ./hello_world 
RUN chmod 400 /home/hello_world/flag.txt
RUN chmod 744 ./hello_world.c

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d

