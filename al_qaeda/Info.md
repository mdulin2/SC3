## Isis Blog 
- home page (about us) (static) 
- Blog page (dynamic via mysql) 
  - MySQL injection on this page that can be exploited to steal creds to login :) 
- Add blog post (dynamic with HTML) 
- Login page (username and md5 hash for storage) 
  - hashing: hashing: 
  - admin: almostthere
- Admin page (flag and add blog post/add users)
- Registration: 
  - Not included by default...


### Turn on the Blog 
Run the following command while in the 'src' directory:
```
sudo docker run -i -t -p "80:80" -v ${PWD}/app:/app -v ${PWD}/mysql:/var/lib/mysql mattrayner/lamp:latest
```

Login to the instance: 
```
sudo docker exec -it <instance_name> /bin/bash
```