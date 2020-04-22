'''
DO NOT MODIFY THE CLIENT.... THERE IS NO REASON TO MODIFY THIS CLIENT THROUGHOUT THE CTF.
Usage: 

python client.py <IP> <PORT> <FILENAME>

- IP: The ip address/domain to connect the client to. 
- PORT: The port of the IP address to connect to . 
- FILENAME: The name of the file to send.

'''
import socket
import sys 

# Check CLI parameters
if(len(sys.argv) != 4):
	print("python3 client.py <IP> <PORT> <file_name>") 
	sys.exit(0)

# The three CLI parameters
IP = sys.argv[1] 
PORT = sys.argv[2]
FILENAME = sys.argv[3]

s = socket.socket()
s.connect((IP,int(PORT)))

print("Opening file...") 
f = open (FILENAME, "r")
line = f.read(1024)

print("Sending the file...")
while (line):
    s.send(line)
    line = f.read(1024)

s.shutdown(socket.SHUT_WR)
print("Sent file!")
reply = s.recv(1024) # Feedback: would like the receive feedback from the server.

print("Execution output: \n")
print(reply)
s.close()

