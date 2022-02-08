## Solution 

### Overview 
- The purpose of this challenge is to force students to either use CURL or postman to make a request to a server that is not a GET requst in the browser.
- So, there are two requests that students must make: POST and DELETE.


### Solution Code
- The solution here will be using CURL. But, there are multiple ways to solve this: 
- POST request: 
	- `curl -X POST '<<domain:port>>/route1'`
- DELETE request: 
	- `curl -X DELETE '<<domain:port>>/route2'`
- Each of these requests gives half the flag. In order to get the full flag, combine the two with the flag with 'flg{' (POST) first.
