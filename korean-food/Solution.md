# Solution 
The goal of the challenge is to become the administrative user on the site. This challenge has been slightly altered from the previous two years for a fun way to become admin! :)   
  
The request to create a user has three parameters: username, password and *is_admin*. By default, the *is_admin* field is set to   
false. However, if you make the request with this set to *true*, the user is NOW an admin user on the site.   
  
There are few ways to go about this:   
- Manually make a request in cURL with *is_admin* set to *true*.
- Intercept the request with a proxy (such as Burp Suite) to change the *is_admin* parameter to be true. 
- In the network tab of the browser dev tools, make a request to register a user. Then, right on the request to have the   
  *Edit and Resend* option appear. Use this option to resend the request with *is_admin* set to true. 

Here's a programmtic example (with cURL) making the request to create an admin user. NOTE: The name of the user must be unique for this to work.
```
curl 'http://18.216.254.83:3001/register' \
-H 'Content-Type: application/json;charset=utf-8' \
--data-raw '{"username":"hackerman","password":"man","is_admin":true}'
```

Once the administrative user has been created, the '/korean_food' page will have the flag ready to go :) It's displayed   
in the korean food table as any other entry!


## Winning 
- Once the application believes that the admin user is being used, it will output the flag on the next search that is done. 
