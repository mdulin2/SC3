## Solutions 
- This is a list of solutions to various Linux challenges.

### first_ssh 
- Login using SSH
- This can be done with ssh first_ssh@<ip> -p 2226
	- The password is the same as the username.
- Then, use a program to display the output: 
	- ``cat flag.txt`` is an example of this.
- SC3{FIRST_SSH!}

### deeper 
- Same as the previous challenge but you need to move a single directory into ``directory1``. 
- Two flows: 
	- ``cat ./directory1/flag.txt``
	- ``cd ./directory1; cat flag.txt``. 
- SC3{A_l1TT13r_b1t_HA7d3R_N0w!}

### processes
- At the beginning of the Dockerfile, a script is ran that puts a `secret` into a CLI parameter. 
- In order to see this, we can use the ``ps`` command in order to see all of the running processes on the box.  
- To see the full output, run ``ps -av`` with a fairly wide terminal screen: 
	- ```  
	PID TTY      STAT   TIME  MAJFL   TRS   DRS   RSS %MEM COMMAND
    1 pts/0    Ss+    0:00      0     0  4636   872  0.0 /bin/sh -c /start.sh
    7 pts/0    S+     0:00      0     0 18384  3068  0.0 /bin/bash /start.sh
    8 pts/0    S+     0:00      0     0 18384  3128  0.0 /bin/bash /home/processes/ps_fun.sh SC3{Hijack_the_flowzzz}
   30 pts/0    S+     0:00      0     0  4540   856  0.0 sleep 5d
   31 pts/1    Ss+    0:00      0     0 18516  3384  0.0 /bin/bash
   70 pts/2    Ss     0:00      0  1037 19326  3836  0.0 -bash
   96 pts/0    S+     0:00      0     0  4540   776  0.0 sleep 1
   97 pts/2    R+     0:00      0   109 27594  1552  0.0 ps -av
   ```
- One of the processes will be our continued script execution. The CLI parameter for this is the flag:
	- NOTE: The terminal needs to be WIDE. Otherwise, the full command output will NOT be printed. 
- SC3{Hijack_the_flowzzz}
