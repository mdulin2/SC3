## Othello 
- This is an A.I that I wrote for the board game Othello when I (Max Dulin) was in college. 
	- https://github.com/mdulin2/Othello
	- This repo has a slightly modified version of the repo in order to display a flag.
- The goal is to beat this A.I.

## Setup 
- Download the Othello repo (shown above) 
	- NOTE: Small changes have been made in order to make the gameplay more seamless for the students and deliver a flag upon winning.
- Install pypy (JIT python, which is much faster) 
- Run the socat command expose setup the service to be usable remotely: 
	- `socat TCP-LISTEN:6000,fork,reuseaddr EXEC:"python -u game.py"`. 
	- NOTE: The '6000' is the port being listened on 
	- NOTE: The '-u' on the Python disables output buffering, making the service possible on a network.
- Connect to the service via netcat (nc <IP> <PORT>) 
- Play the game!
