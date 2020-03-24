## Solutions 


### Firsty 
- Just enter in 16 characters. This will overflow the string variable. Then, this will overflow the integer variable that was originally set. 


### Dead 
- A little bit more tricky! 
- `python -c 'print "A" * 8 + "\xef\xbe\xad\xde"' | ./dead`. 
- The overflow is the same as before. But, instead, we are using the overflow to set the integer value to something! The char array is 8 bytes (1 * 8 = 8). Then, the integer is 4 bytes long. 
- The ordering looks weird! This is because of endianess :) 
