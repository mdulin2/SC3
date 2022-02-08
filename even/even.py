#!/usr/bin/python

import os
import pwd

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

def is_even(char):
	if(ord(char) & 0x1 == 0x0):
		return True
	return False

def is_valid(user_input):
	for char in user_input:
		if(is_even(char) == False):
			return False

	return True


def run():
	print(get_username())

	#print 'uid,euid =',os.getuid(),os.geteuid()
	#print 'gid, egid', os.getgid(),os.getegid()
	input_data = input("Command String:")
	if(is_valid(input_data)):
		os.system(input_data) 
	else:
		print("Invalid!") 
run()
