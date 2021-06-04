## JWT Challenge
JWTs are a common way to authorize uses. The information is stored on the client side.  
The way that they are secured is by using a cryptographic signature. Because the user does not 
know the secret, this makes it impossible to alter.    
  
Created by Rachael Hardin from SI

There are three flags here: 
- One for logging in and visiting the private endpoint (easy) 
- One for decode the JWT
- One for cracking the secret on the JWT to create an 'admin' token. 

## Flag 1
Log in using the /login endpoint, with the link of the main index page. This will set the 'jwt'   
in the application cookies under 'session'. provide the token in the URL on the /private endpoint.  
As long as the token is valid (6 minutes) the user will be presented with a flag as they have   
successfully authenticated. This is a gimme!

## Flag 2
The JWT itself is a base64 encode collection of JSON objects. The JWT itself should on contain   
any secret information when used in a real environment. 
  
To get the flag, base64 decode the content. This can be done with Python, cyberchef, jq and other things.  
The best (and nicest) way to see the data is at https://jwt.io/. This decodes the token and shows the   
fields in a very nice way. 

## Flag 3
The /admin endpoint checks for a JWT with a username of 'admin' AND validates the JWT signatures.   
Because the signature check is done, the only way to be able to craft a fake token is to *crack the secret*.   
  
Players will need to crack the secret key ('secret', should crack in about 5 seconds with rockyou.txt)   
to create their own JWT. What's the easist way to do this crack!? Well, there are a few ways. 
  
The creator of this challenge (Rachael Hardin) created a few scripts for doing this. The solution for
BOTH cracking the secret and signing the secret are in interactive Python scripts under 'solutions_scripts'.   
  
The other way to go about this is to use one of the off the shelf tools to do the cracking. The tool   
https://github.com/ticarpi/jwt_tool works quite well for this purpose (and signing as well). The command   
for using this tool looks like the following:   
```
python3 jwt_tool.py <token> -C -d rockyou.txt
```
The list of secrets to guess can be found with the standard *rockyou.txt* wordlist.   
https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou-50.txt is a good   
locaiton to find it, if somebody is having trouble.   
Either way, the secret that will be spat out is ``secret``, which is super fitting.   
  
Once we have the secret, we need to `sign` the JWT with the ADMIN user. This can be done using ``jwt_creator``   
in the 'solutions_script' directory, by going to https://jwt.io with the secret and the value to modify with   
or a plethora of other tools.   
  
With the secret in hand, set the value of the `session` cookie to be the newly created JWT. Now, when going to   
the 'admin' endpoint, you'll be greeted with the flag. 
