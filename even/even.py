import os

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
	input = raw_input("Command String:")
	if(is_valid(input)):
		os.system(input) 
	else:
		print "Invalid!"
run()
