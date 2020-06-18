## Overview 
- Simple site that gets images or other files and saves it for a user. 
	- The image/file gets rendered for the user (nailtereset) 
- This is vulnerable to SSRF 
- Have a local server running that has endpoint at localhost/flag.txt
	- This will also for the flag to be exfiltrated.

### Implementation
- Authentication model: A magic link to edit data in the future: 
	- Did not want to implement a full authorization scheme
- Storage:
	- ONLY storing links for a user
	- Magic link to user combination
- Web Server: 
	- localhost server: at localhost:80/flag.txt
	- backend: flask server with 5 API endpoints
		- Create User 
		- Add Link 
		- Get links for user 
		- Get all users 
		- Process link
	- frontend: 
		- Home (shows all profiles)
		- Add link to user 
		- Create user page
		- My Profile (displays all links via pictures or text) 

