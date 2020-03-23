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


## Potential Challenges 
This is organized in the following way: the type of challenge and the difficulty in creating the challenge.   
Additionally, the bolded challenges have already been created. 

- Insecure Wordpress extension (RCE or something) (8)
- Bad switch statement (4) 
- CRLF injection (?)
- HTTP smuggling (11)
	- Probably not something to do...
- Android connection emulation (10)
- Buffer Overflow series (6): 
	- Alter a variable on the stack 
	- Write a proper variable on the stack (Done) 
	- Redirect execution of the binary to a new function (auth, but diff) 
	- Shellcode/ROP
- Writing assembly to open a file (4) 
- Template injection (5)
- Math: 
	- Statistics math problems (? -Jeb)
	- Combinatorics
- Bypassing restrictions by patching binaries (4)
- Insecure file upload (6)
- Simple IDOR (6)
- Parameter tampering on POST request (use BURP :)) (4)
- CSRF (manually verify)(6)
- Filter bypass on regex (5)
- AWS Priv Esc (7)
- Host header injection for an email reset link (5)
- Facial recognition bypass (Sebs react app. Can use a picture of someone!)(ask Sebs) (7)
- Request type implicit assumption (if not post, then get). (5)
- Fun heap corruption (2)
- Shellcode writing (3)
- Bad C parsing for a somesort of file format (?)
- Bad default handling (6) 
  - Unsure what to do here...
- Relative file path issues (symbolic links)(6)
- Digital Signatures or HMACs (manually verify) (3)
- **Exploit mitigations (manually verify)**
	- (NX, ASLR, Stack Canaries)
- Blockchain challenges (resuse SI's setup) (10)
	- Hopefully get Ben Stewart to set this up
- OSINT (5):
	- Private key for server 
	- Password reset info
- **Beating Max Dulin A.I for Othello**:
	- https://github.com/mdulin2/Othello
	- Just a previous school project 
- Format string vuln (write or read) (7) 
- Source code analysis (manual verification) (6):
- DoS (based upon timeout) (8)
- Bad usage of crypto (hashes when random should be used?) 
- File descriptor bug
- Secrets in log files for some website 
- Memory corruption via driving game with ASCII graphics  (9) 
- **OTP bypass by flooding to increase likehilhood of login** 
- **Error message into code exec**: 
- Log analysis (Corey?) 
- Memory Forensics (Gerard?) 
- Soldering (?) 
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
		
