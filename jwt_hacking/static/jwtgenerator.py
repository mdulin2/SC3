#!/usr/bin/env python

import jwt
from datetime import datetime, timedelta

print("JWT Generator")

raw_payload = {
    "user" : "<INSERT YOUR USERNAME HERE>"
    "iat" : datetime.utcnow(),
    "exp" : datetime.utcnow() + timedelta(seconds=3600)
}

payload = jwt.encode(raw_payload, None, algorithm='HS256')
print("Your encoded JWT is ... [" + payload + "]")
