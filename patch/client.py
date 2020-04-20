#client 
# python3 client.py 
# TODO: Add a parameter for the user file 

import socket
s = socket.socket()
s.connect(("localhost",3000))

print("Opening file...") 
f = open ("easy_auth", "r")
l = f.read(1024)

print("Sending the file...")
while (l):
    s.send(l)
    l = f.read(1024)
s.shutdown(socket.SHUT_WR)
print("Sent file!")
print("Execution output: \n")
reply = s.recv(1024) # Feedback: would like the receive feedback from the server.
print(reply)
s.close()
