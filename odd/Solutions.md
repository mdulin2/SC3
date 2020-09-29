# Overview
- Restrictions: 
	- Only can use characters that end with a '1'. 
- What does this do: 
	- No wildcard (' * ') and no space!
	- So, we cannot provide a parameter to these functions haha
	- '.' is not allowed
- What do we have? 
	- / (allows for directory traversal!) 
	- a,c,e,....
	- ? (single character wildcard) 

## Solutions
### Execute script
- Not allowing for the ability to write to the directory, but WOULD work 

### Vim 
- /us?/?i?/?im
- Then, run bash command from inside of here
	- :!cat flag.txt

### Ed 
- /?i?/e?
- Then, run a bash command from inside of here
	- !/bin/sh

### Emacs
- emacs (happens to only have good characters!) 
