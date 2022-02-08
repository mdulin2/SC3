# SC3
The third occurence of the Spokane Mayor's Cyber Cup! Here's to another great year :)  
  
## Organization 
Organization in this is CRUCIAL. Please adhere to the following when writing a challenge. Each directory comes with the following: 
- *Challenge* file
- *Solution* file
- Optional *Info* file (for setup details and other notes) 
- *Challanges* themselves. 
- ``Dockerfile`` and ``docker_run.sh``

Some challenge directories will have multiple challenges in one. For instance, the Forensics and log analysis questions will have multiple challenges per directory. The Challenge.md will have these labeled as seperate challenges and the Solutions file will have multiple answers, each corresponding to the solutions.    

## Challenges
This is organized in the following way: the type of challenge and the difficulty in creating the challenge.   
Additionally, the bolded challenges have already been created.   
  
If somebody has ANY other ideas, then please go crazy and create the challenge! These are just thoughts that I (Max) had and put down before I forgot. All types of challenges will be accepted (even some Stegography). 
  
The goal is to have something like 30-40 challenges from all different categories. Currently, the total amount of finished flags is 37.
- Web: 14
- Binary/Memory Corruption: 6
- Reversing: 4
- Linux: 7
- Cryptography/Math: 1
- OSINT: 4
- Blue Team: 6
- Misc: 2 (random things that do not have a particular category) 

## Running Challenges
- The challenges fall into 4 categories: 
	- SSH - Login to solve the challenge
	- Remote pwnables: Interact with the service via netcat
	- Web - Website
	- Other - Files or prompt in the challenge. 
- For all but the final section, simply running ``./docker_run.sh``  will build and run the Docker container. This will then be accessible via the mentioned port in the script. 

### Web 
- **Al Qaeda Blog** 
	- SQLi to get a flag from the database (4)
	- SQLi to leak admin password hash (7)
	- Crack MD5 hash (5) 
- **POST_DELETE**: 
	- Make POST and DELETE requests to an endpoint
- **Nailterest**:
	- Storage of favorite links (pictures, text files, etc.)
	- Use this feature to grab data from a localhost server that is running. This is also known as SSRF.
- **JWTs** (Rachael Hardin):
	- Login (2)
	- Decode JWT (4)
	- Crack and resign (8) 
- **Parameter tampering on POST request** (5): 
	- Korean food challenge but set the *is_admin* flag to true to become an administrator.  
- **Lebean** (Ken Price):
	- Simple XSS (4) 
	- Double quote escape (5) 
	- Single quote escape (5) 
	- Template string escape (7) 
	- Javascript URI link (7) 
- Lottery (Vanessa Dulin):
	- Cracking the lottery via an insecure random number generator. 

### Memory Corruption
- Buffer Overflow series (buf_series)(6): 
	- **Firsty**
		- Alter a variable on the stack
	- **dead** 
		- Write a proper variable on the stack**
	- **auth** 
		- Redirect execution of the binary to a new function
- **HelloWorldArg** 
	- Format string vuln 
- **Floating Bank**:
	- Improper usage of floating point numbers

### Linux
- **signals**: 
	- Sending a signal to continue a flag 
- Basic Linux Commands (introduction to Linux) 
	- **ssh**
	- **process names**
	- **Moving directories**
- **amazon** 
	- OTP bypass by flooding OTP values
- **error_to_code** 
	- Error message into code exec
- **auth_handler** 
  - Try catch block with an initally set value.
  - Convert input to an integer, then use this as a case statement to determine auth level
  - With the originally set value of the int (0), this could act as a bad default handling
- **even**:
	- Run bash commands with either ONLY odd or even characters. 
	- Even is MUCH harder than odd because the / cannot be used with even.
- Linux Hardening 

### Reversing (Zach) 
- **1: First reverse**
- **2: xor flag**
- **3: Rolling xor flag**
- **Patch**
	- Bypassing restrictions via altering the binary itself.
	
### Misc
- **Othello**:
	- https://github.com/mdulin2/Othello
	- Just a previous school project from Max Dulin. 
	- It has been thrown in here for a fun little challenge to learn a fun board game
- **Astros** 
	- Pattern recognition for stealing signs in baseball

### Blue Team 
- Malware Forensics (6) 
	
### Crypto/Math Math: 
- Cesar Cipher 

### OSINT
- Location problems (3) - Fabian Vilela
- Find person via photo - Joseph Riddle


