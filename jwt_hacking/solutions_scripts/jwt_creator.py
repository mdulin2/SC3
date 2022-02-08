#!/usr/bin/env python

import jwt
from datetime import datetime, timedelta

print("JWT Generator")

username = input("Username (admin?): ")
secret = input("Secret for signing: ") 
raw_payload = {
            "user" : username, 
            "iat" : datetime.utcnow(),
            "exp" : datetime.utcnow() + timedelta(seconds=3600)
            }

payload = jwt.encode(raw_payload, secret, algorithm='HS256').decode('utf-8') 
print(payload) 
