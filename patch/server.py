import socket
import sys
import subprocess 
import os
import random
import string 

# TODO: Add properly error handling for the main server 

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

# Runs the web server
def main():
    s = socket.socket()
    s.bind(("localhost",3000))
    s.listen(10)
    i=1
    while True:
        print("Connection has been made...")
        # Insert a random number... Create this as a file
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

    s.close()


main() 
