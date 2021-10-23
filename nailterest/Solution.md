# Nailterst Solution 

## Overview
- This is a social media platform that is honest about data always being here. It has five pages: 
	- home (shows all other profiles) 
	- profile (shows all links for a user) 
	- create (create an account) 
	- add (add a link to a profile) 
	- info (information about the platform)

## Solution 
- Images and text files are processed in different ways. 
	- Images: Processed with a GET request directly from the site. 
	- Text (.txt and md): A request is made on the **backend**. Then, the data is sent back to the frontend, after being processed.
- The **text** file is processed with a request from the backend. This means that the request has access to the LAN (local area network). 
	- Some services are only available on the LAN, but not the *wide area network*.
	- Being able to make requests on the LAN allows us to access services on the LAN from the WAN!
- There is a server running on localhost:1337 on the LAN with an endpoint at /flag.txt.
FLAG: 
	- Adding a link to *http://localhost:1337/flag.txt* will output the flag on the profile page.
	- flg{sErv3r_31De_ReqUest_FForgery_1s_A_BBBIIGGG_Dea!}


	
