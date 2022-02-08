## Information (might not use this one):
There are two ways that this program could work: 
- Run the load of the flag AFTER the raise function (with no print) 
- Run the load of the flag AFTER the raise function (with the print) 
  
The first configuration would give out a CORE dump. This core dump would have the flag in it.  
The second configuration would be about handling signal processes.

### Current Configuration 
- The current configuration has the first configuration, which forces people to learn how to use core dumps.
