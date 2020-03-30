## Solution 

The purpose of this challenge is to get students to learn about signals and syscalls. 

## What is Happening? 
- First, we call fork on the process. This starts a new process off of the parent process: 
	- The parent process returns the pid of the child process. 
	- The child process return the pid of 0. This is how we know which process is which in the code. 
- The child process will send the signal (SIGSTOP) to itself. This essentially pauses this process.
- The parent process will send (with the kill function) a signal call and a process id, which are both specified by the user

## Solving
- The child process sends itself the signal SIGSTOP, which pause the program until something tells it to continue. 
	- So, how do we get this process to continue? 
- The `kill` function sends a signal to a particular process. The function looks like this: kill(pid,SIGCALL)
- By sending the child PID (which is printed) and the SIGCONT (18) signal to the program, the child process will continue executing. 
- Now, the flag should print!


For more on signals learn at these places: 
- https://www.usna.edu/Users/cs/aviv/classes/ic221/s16/lec/19/lec.html 

For the actual signal call information: 
- http://man7.org/linux/man-pages/man7/signal.7.html

