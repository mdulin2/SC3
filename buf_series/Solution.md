## Solutions 
- This is a list of solutions to various *buffer overflow* challenges. 
- This is meant to ease students into the area, instead of drowning them on redirecting execution right away

### Firsty 
- The buffer is 8 characters long but accepts 16 characters. What happens if we write more than 8 characters? 
- The stack is setup in the following way:
	- cool_string 
	- cool_int 
- So, when the string gets added with more than 8 characters, then **cool_int** is overwritten!
- Simply corrupting this value is enough to pass the challenge.


### Dead 
- A little bit more tricky! 
- The overflow is the same as before, with the same stack setup. 
- But, instead, we are using the overflow to **set** the integer value to a specific value! The char array is 8 bytes (1 * 8 = 8). Then, the integer is 4 bytes long.
- There are two main tricks to this: 
	- Writing the bytes properly 
	- Endianness
- Writing bytes: 
	- We are trying to write the integer 0xdeadbeef into memory.
	- The hex stream \xef is not a normal character. So, how do we write this? 
	- In Python (Python 2 at least) you can write escaped bytes with hex codes. 
	- Python example: print "\xef" 
		- This would print the literal byte 0xef
	- Common: 
		- Students will try to print the literal 0xdeadbeef. This will not work because this is intertuped as an integer.
- What is endianness? 

	- The ordering in which bytes are organized in memory. x86 is little Endian, meaning that the least significant byte appears first.
	- So, with 0xdeadbeef, we need to write this in the following way: 0xefbeadde. 
	- Remember, we are writing BYTES. 0xef is a SINGLE byte still.

- Final payload:
	- `python -c 'print "A" * 8 + "\xef\xbe\xad\xde"' | ./dead`
	- Prints the proper bytes (with the Python hex escaping) and prints it in the proper Endinness.

