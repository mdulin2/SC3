## Solution 
- Signals are normally from the kernel. They are used to convey from userland (the normal using processes) and the kernel (between userland and the hardware) what a system call has resulted in. 
- However, signals can also be sent from userland to userland processes (even for itself). 
- Different signals have different 'actions' that result from the signal. These actions are 'Terminate', 'Core Dump' 'Stop' and 'Ignore'.
- The different signals (going to a process) can actually be handled, in some cases. 
- So, in order to handle signal 25, open up program in a subprocess which can handle it.
- The following code below handles the signal: 
``` 
python -c "import subprocess; subprocess.Popen(['./sig', '']); exit()"`
```
