# SC3
The third occurence of the Spokane Mayor's Cyber Cup! Here's to another great year :)  
  
## Organization 
Organization in this is CRUCIAL. Please adhere to the following when writing a challenge. Each directory comes with the following: 
- *Challenge* file
- *Solution* file
- Optional *Info* file (for setup details and other notes) 
- *Challanges* themselves. 
- *Coming Soon* - Dockerized version of the challenges (that needed to be Dockerized, that is) 

Some challenge directories will have multiple challenges in one. For instance, the Forensics and log analysis questions will have multiple challenges per directory. The Challenge.md will have these labeled as seperate challenges and the Solutions file will have multiple answers, each corresponding to the solutions.    


## Improvements 
- GET MORE PEOPLE INVOLVED writing challenges
- Recruit early and often 
- Bigger than last year 
- Dockerize everything (Vanessa Nguyen) 
- Test challenges from the testing location (EWU) 
- More diverse (schools, ethnicity, gender, etc.) 

## Potential Challenges 
This is organized in the following way: the type of challenge and the difficulty in creating the challenge.   
Additionally, the bolded challenges have already been created.   
  
If somebody has ANY other ideas, then please go crazy and create the challenge! These are just thoughts that I (Max) had and put down before I forgot. All types of challenges will be accepted (even some Stegography). 
  
The goal is to have something like 30-40 challenges from all different categories. Currently, the total amount of finished flags is 35.
- Web: 13
- Binary/Memory Corruption: 8
- Reversing: 4
- Linux: 7
- Blockchain: 0 
- Cryptography/Math: 1
- Blue Team: 0 
- Misc: 2 (random things that do not have a particular category) 


### Web 
- **Al Qaeda Blog**
	- SQLi to get a flag from the database (6) 
	- Leaking credentials to get one of the flags (7) 
- **POST_DELETE**: 
	- Make POST and DELETE requests to an endpoint
- **Nailterest**:
	- Storage of favorite links (pictures, text files, etc.)
	- Use this feature to grab data from a localhost server that is running. This is also known as SSRF.
- **JWTs**: 
	- Login (2)
	- Decode JWT (4)
	- Crack and resign (8) 
- **Parameter tampering on POST request** (5): 
	- Korean food challenge but set the *is_admin* flag to true to become an administrator.  
- **Lebean**:
	- There are 5 challenges in here!
	- Simple XSS (4) 
	- Double quote escape (5) 
	- Single quote escape (5) 
	- Template string escape (7) 
	- Javascript URI link (7) 
- Lottery (Vanessa): 
	- Cracking the lottery via an insecure random number generator. 
- Facial recognition bypass (Sebs react app. Can use a picture of someone for facial recognition!)(ask Sebs) (5)
	- https://github.com/sebvargas/MLFacialRecognition/blob/master/InstallationDocs.md
- Web Scrapping Challenge(6) (Andrew): 
	- Get a speed of xyz by scripting the entire thing.
- Simple IDOR (6)
- Regex Bypass Quiz (5)
- Source code analysis (manual verification) (6)
- Host header injection for an email reset link (5)
- Insecure file upload (6)
- Client Side Trust of Bar Codes (9): 
	- Bar codes hold data. But, this data is known and cannot be trusted by itself. 
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

### Memory Corruption
- Buffer Overflow series (buf_series)(6): 
	- **Firsty**
		- Alter a variable on the stack
	- **dead** 
		- Write a proper variable on the stack**
	- **auth** 
		- Redirect execution of the binary to a new function
	- Shellcode/ROP
- **Exploit mitigations (manually verify)**
	- NX 
	- ASLR 
	- Stack Canaries
- **HelloWorldArg** 
	- Format string vuln 
	
### Linux
- **signals**: 
	- Sending a signal to continue a flag 
- Basic Linux Commands (introduction to Linux) 
	- ssh 
	- process names 
	- Moving directories
- **amazon** 
	- OTP bypass by flooding OTP values
- **error_to_code** 
	- Error message into code exec
- **auth_handler** 
  - Try catch block with an initally set value.
  - Convert input to an integer, then use this as a case statement to determine auth level
  - With the originally set value of the int (0), this could act as a bad default handling
- Relative file path issues (symbolic links)(6)
- **Finally Switch**: 
	- Python command injection into ``input``. 
- **odd/even**:
	- Run bash commands with either ONLY odd or even characters. 
	- Even is MUCH harder than odd because the / cannot be used with even.

### Reversing (Zach) 
- **1: First reverse**
- **2: xor flag**
- **3: Rolling xor flag**
- **4: Packer and rolling xor flag**
- **Patch**
	- Bypassing restrictions via altering the binary itself.
	
### Misc
- **Othello**:
	- https://github.com/mdulin2/Othello
	- Just a previous school project from Max Dulin. 
	- It has been thrown in here for a fun little challenge to learn a fun board game
- **Astros** 
	- Pattern recognition for stealing signs in baseball
- OSINT (5):
	- Private key for server 
	- Password reset info
- Memory Forensics (Gerard?) 
- Soldering (?) 
- Lock Picking

## Blockchain (Ben) 
- Blockchain challenges (resuse SI's setup) (10)
	- Hopefully get Ben Stewart to set this up
	- Looking at 3-4 blockchain based challenges for this contest. 
	
### Crypto/Math Math: 
- Statistics math problems (? -Jeb)
- Elliptic Curves (Jeb) 
- **Passphrases**: 
	- Map passphrase to key without decoding code
- Combinatorics
- Digital Signatures or HMACs (manually verify) (3)
- Cesar Cipher 
- Brute force RSA private key given the public key (small) 


### Blue Team 
- Secrets in log files for some website 
- Log analysis 
- Others.. Corey? 
- Mitigation (firewall rules or something?) 
