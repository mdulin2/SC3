FROM ubuntu:16.04

RUN apt-get update && apt-get -y install build-essential gcc socat python
ADD othello /Othello
ADD flag.txt /Othello/flag.txt

# Runs the program for all people to conenct to on port 6969
ENTRYPOINT socat TCP-LISTEN:10005,reuseaddr,fork EXEC:"python -u /Othello/game.py",pty,stderr
