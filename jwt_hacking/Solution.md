There's three possible flags here:  

1) Log in, provide the token in the URL on the /private endpoint. As long as the token is valid (6 minutes) the user will be presented with a flag as they have successfully authenticated. This is a gimme.

2) Decode the JWT, either with Python, jwt.io, cyberchef or equivalent. There is another flag inside the JWT.

3) The /admin endpoint checks for a JWT with a username of 'admin' but also validates JWT signatures. Players will need to crack the secret key ('secret', should crack in about 5 seconds with rockyou.txt) and create their own JWT in order to get this one.