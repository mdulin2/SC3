'''
python3 server.py 
	- Make sure that the script has access to the ./tmp folder. Otherwise, the program will crash.
'''

import socket
import sys
import subprocess 
import os
import random
import string 
from threading import Thread, Event
import time

# Validate that the bytes of the file are extremely close in size
def validate(filename):
    original = "./easy_auth" 

    # Open the two files 
    f_og = open(original, "rb")
    f_new = open(filename,"rb") 

    # Setting up the beginning values 
    difference = 0 
    amount = 0
    byte_og = f_og.read(1)
    byte_new = f_new.read(1) 
    while((byte_new and byte_og) and difference <= 10): 

        # If the byte difference is 10 or larger.
        if(difference == 10): 
            return False 

        # Compare each byte of the file byte by byte
        if(byte_og != byte_new):
            difference += 1

        byte_og = f_og.read(1)
        byte_new = f_new.read(1) 
        amount += 1

    # Close the fd's
    f_og.close() 
    f_new.close() 

    # Ensure that the values are large enough
    if(amount < 10): 
        return False 

    return True 

# Executes the code and returns the result
def execute(filename):
    os.chmod(filename,777)
    output = subprocess.check_output([filename])
    return output 

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Runs the main server on loop 
# s: Socket object 
def server(s=None,sc=None):
    print("Connection has been made...")
    sc, address = s.accept()
            
    # Generate the random file 
    newfile = "./tmp/" + randomString()
    f = open(newfile,"bw") # open in binary

    line = sc.recv(1024)
        
    # Write to file, recieving 1024 bytes at a time.
    while (line):
        f.write(line)
        line = sc.recv(1024)
    f.close()
        
    # If the files are more than 10 bytes different
    # Validate the files 'byte-by-byte' (try to find files less than 10 bytes in difference
    if( not validate(newfile)):
        sc.send(bytes("Files too different...exiting.", "utf-8"))
        os.remove(newfile)

    # If the file is valid or not. 
    else:
            # Execute the code and return the output to the client
        output = execute(newfile)               
        os.remove(newfile)
        sc.send(output, 1024) # Would like to send back a response

    sc.close()

# Runs the web server
def main():
    s = socket.socket()
    s.bind(("localhost",3004))
    s.listen(10)

    # Runs the main server in a loop.
    # Moved this to its own function in order to have timeouts initiated with try-catch blocks...    
    while(True): 
        try:
            
            # The main server component, with a built in timeout feature 
            thread = Thread(target=server,kwargs=dict(s=s))
            thread.start() 
            thread.join(timeout=5)

        # Quit the service after a keyboard interrupt (nice for testing)
        except KeyboardInterrupt:
            raise
        except: 
            print("Something went wrong on the call...")

    s.close()


main() 
