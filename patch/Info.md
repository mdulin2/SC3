## Patch 
- The goal is to ensure that the students patch a file and send this to the server (then, the code is executed).
- How (with safety): 
	- Send the binary to a server (with pre-built scripts) 
	- Do a check on the byte similarity (only allow 10 bytes of difference?) 
- If the bytes are VERY similar, the code should run okay.

### Files 
- client.py: The client for the user to connect to in order to send the file.
	- format: python client.py <IP> <PORT> <FILENAME>
- server.py: The server which validates and executes the binary 
- easy_auth.c: 
	- The source code for the file
	- Prior giving out, remove the 'test' function from the source code. This makes it impossible to recompile the source code.
- easy_auth: The binary to give to the students 
- patched_auth: A potential solution to the challenge
- flag: The flag for the challenge
- Solution.md: The solutions to the challenge 
- Challenge.md: The challenge to the student
