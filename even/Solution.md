## Overview
- Get the flag, with only even characters!
- Restrictions: 
	- ' ? ' 
	- '/' - Makes it impossible to use wildcards for names
	- a,c,e,... i and o cannot be used either. This makes it REALLY hard
	- Dashes ('-') makes flags impossible to use
- Forced to use SMALL commands with no vowels
- A good list of these can be found at https://gtfobins.github.io/.

## Solutions
### hd
- hexdump!
- hd *
	- Prints a hexdump of the flag
- Output is large. Since all flags begin with 'SC3', we can grep for that: 
	- ``echo "hd *" | ./run | grep 'SC3' -A 2``
00000210  75 6e 28 29 0a 53 43 33  7b 65 76 65 6e 5f 49 73  |un().SC3{even_Is|
00000220  5f 6e 6f 74 5f 6f 64 64  21 67 6f 74 74 61 5f 6c  |_not_odd!gotta_l|
00000230  6f 76 65 5f 74 68 65 5f  2a 7d 0a 7f 45 4c 46 01  |ove_the_*}..ELF.|

### pr
- This command is used for converting text files into hex data or something like that
- pr *
	- Will print the hex data of all files in the folder!
	- ``echo "pr *" | ./run | grep 'SC3' -a``

### ptx
- produce a permuted index of file contents
- ptx *
	- Print out all file contents
	- ``echo "ptx *" | ./run | grep 'SC3' -a``
	- SC3{even_   Is_not_odd!gotta_love_the_*}

