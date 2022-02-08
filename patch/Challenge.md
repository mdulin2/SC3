## Challenge 
- You have been given a file with protections on it... Can you ALTER the binary in order to get it to execute the other part of the if statement? In order to execute the binary, send it to <IP> with the client.
- Use the 'client.py' to send files to the server with the altering file.
	- Format: `python client.py <IP> <PORT> <FILENAME>`
- Hint: 
	- This is known as 'patching'
	- There are several ways to do this, the Live Overflow video gives a few. 
		- https://www.youtube.com/watch?v=LyNyf3UM9Yc
	- Linux only tools: 
		- objdump 
		- hexdump 
		- xxd

- Given: 
	- Source code for easy_auth.c (with test function removed) 
	- client.py 
	- easy_auth
