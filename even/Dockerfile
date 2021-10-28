FROM ubuntu:18.04

# Add GDB, Python, SSH, gcc and curl
RUN apt-get update -y && DEBIAN_FRONTEND="noninteractive" TZ="America/New_York" apt install openssh-server g++-multilib vim gcc python git curl bsdmainutils nano tmux perl build-essential emacs vim -y

# Setup the users
## Setup the 'even' user to login with
RUN useradd -d /home/even/ -m -p even -s /bin/bash even
RUN echo "even:even" | chpasswd
RUN chown -R root:even  /home/even

## Setup the user that owns the flag
RUN useradd -d /home/flag_user/ -m -s /bin/bash flag_user
RUN chown -R root:flag_user  /home/flag_user


# Copy in the files
ADD even.py /home/even/even.py
ADD run.c /home/even/run.c
ADD ./flag.txt /home/even/flag.txt

RUN gcc /home/even/run.c -o  /home/even/run -m32 -ggdb -O0

# Setup the proper file for each set of exercises
RUN chown root:even /home/even/run
RUN chown root:flag_user /home/even/flag.txt
RUN chown root:flag_user /home/even/even.py

# Setup the permissions for the process. Difference between flag_user and even is ability to read the 'flag'
RUN chmod 6755 /home/even/run
RUN chmod 440 /home/even/flag.txt
RUN chmod 744 /home/even/run.c
RUN chmod 744 /home/even/even.py

# SSH server startup. When launching this, specify which port that the SSH (locally port 22) will be bounded to
RUN mkdir /var/run/sshd
EXPOSE 22/tcp 
ENTRYPOINT service ssh restart && sleep 5d

