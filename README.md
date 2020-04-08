# SC3
The third occurence of the Spokane Mayor's Cyber Cup! Here's to another great year :)

Organization
Each directory comes with a challenge file, an Info file and a solution file.
For instance, the easy redirect folder has four files:

flag.py: The web service that gives the flag. In most situations, this will be a text file.
redirect_fun.py: The web service trying to be exploited.
Challenge.md: The challenge/s being given to the contestant.
Solution.md: The solution on how to solve the problem. This is to ensure that the coaches are able to help.
Info.md: How to use the application/challenge.

Some challenge directories will have multiple challenges in one. For instance, the Forensics and log analysis questions will have multiple challenges per directory. The Challenge.md will have these labeled as seperate challenges and the Solutions file will have multiple answers, each corresponding to the solutions.  
 


## Improvements 
- GET MORE PEOPLE INVOLVED writing challenges
- Recruit early and often 
- Bigger than last year 
- Dockerize everything (Vanessa Nguyen) 
- Test challenges from the testing location (EWU) 

## Potential Challenges 
This is organized in the following way: the type of challenge and the difficulty in creating the challenge.   
Additionally, the bolded challenges have already been created.   
  
If somebody has ANY other ideas, then please go crazy and create the challenge! These are just thoughts that I (Max) had and put down before I forgot. All types of challenges will be accepted!


### Web 
- Insecure Wordpress extension (RCE or something) (8)
- CRLF injection (?)
- Bypassing restrictions by patching binaries (4)
- Insecure file upload (6)
- Simple IDOR (6)
- Parameter tampering on POST request (use BURP :)) (4)
- Filter bypass on regex (5)
- AWS Priv Esc (7)
- Basic SQLi (5) 
- Timing based SQLi? (7) 
- Host header injection for an email reset link (5)
- Facial recognition bypass (Sebs react app. Can use a picture of someone!)(ask Sebs) (7)
	- https://github.com/sebvargas/MLFacialRecognition/blob/master/InstallationDocs.md
- Template injection (5)
- Source code analysis (manual verification) (6):
- Typing game (6): 
	- Get a speed of xyz by scripting the entire thing to become the greatest typer ever. 
- Tenent Management/pop quiz
	- First flag (IDOR) 
		- Go from a resident to a building manager/teacher
		- Some vulnerability within this software (I'm thinking an issue with the password reset functionality?) 
		- IDOR on the local manager/teacher password reset? 
	- Second flag (Race condition) 
		- Using binary authorization metrics (read challenges, write challenges, etc) 
		- Race condition on the authorization for users. 
		- When adding a new authorization (by adding a certain value), make a call that will do this not once but twice.
		- This will overall into the next field, which happens to make them an admin (give them the flag at this point) 
		- Permission model based upon bits being set (overflow)
- Curl! 
	- Make a PUT request onto an API? 
		
### Memory Corruption
- Buffer Overflow series (6): 
	- Alter a variable on the stack 
	- Write a proper variable on the stack (Done) 
	- Redirect execution of the binary to a new function (auth, but diff) 
	- Shellcode/ROP
- Fun heap corruption (2)
- Shellcode writing (3)
- Bad C parsing for a somesort of file format (?)
- **Exploit mitigations (manually verify)**
	- (NX, ASLR, Stack Canaries)
- **Format string vuln** (7) 
- Memory corruption via driving game with ASCII graphics  (9) 
- **Race Track** (Heap Memory Corruption) (8) 

### Linux
- **Fun with signal calls**
- Basic Linux Commands (introduction to Linux) 
	- ssh 
	- process names 
	- 2 others? 
- Writing assembly to open a file (4) 
- File descriptor bug
- Bad usage of crypto (hashes when random should be used?) 
- **OTP bypass by flooding OTP values** 
- **Error message into code exec**
- Bad default handling (6) 
  - Unsure what to do here...
- Relative file path issues (symbolic links)(6)

### Misc
- Android connection emulation (10)
- **Beating Max Dulin A.I for Othello**:
	- https://github.com/mdulin2/Othello
	- Just a previous school project 
- OSINT (5):
	- Private key for server 
	- Password reset info
- Memory Forensics (Gerard?) 
- Soldering (?) 
- Blockchain challenges (resuse SI's setup) (10)
	- Hopefully get Ben Stewart to set this up

### Crypto/Math Math: 
- Statistics math problems (? -Jeb)
- Combinatorics
- Digital Signatures or HMACs (manually verify) (3)
- Cesar Cipher 
- Brute force RSA private key given the public key (small) 


### Blue Team 
- Secrets in log files for some website 
- Log analysis 
- Others.. Corey? 
