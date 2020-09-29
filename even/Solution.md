## Overview
- Get the flag, with only even characters!
- Restrictions: 
	- ' ? ' 
	- '/' - Makes it impossible to use wildcards for names
	- a,c,e,... i and o cannot be used either. This makes it REALLY hard
	- Dashes ('-') makes flags impossible to use
- Forced to use SMALL commands with no vowels

## Solutions
### hd
- hexdump!
- hd *
	- Prints a hexdump of the flag
### pr
- This command is used for converting text files into hex data or something like that
- pr *
	- Will print the hex data of all files in the folder!

### tbl 
- Table formatting for froff
- tbl *
	- WIll print all of the files in the folder, including the flag

### ptx
- produce a permuted index of file contents
- ptx *
	- Print out all file contents

