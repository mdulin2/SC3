## Solution 
- The goal is to become a user with level 10, which has two possible scenarios: 
	- Create a user at level 10 
	- Become the root user (id 0) 
- The `Login` function has **default handling**. 
- When a *valid* uid is given (i.e. any integer) then the handling happens totally fine. 
- However, if an invalid uid value (non-number) is used, then the **default** is set to **0**. 
- Because the default uid is 0, then the user becomes the admin user. 
- By selecting option *5* as the admin user, the flag is printed.

