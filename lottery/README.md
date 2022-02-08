# Lottery
- Lottery CTF challenge
- Exploit bad random number generator seeding. 

## Build/Run Steps

```
docker-compose build && docker-compose up  
```

## Proof of Concept

```
import time
from random import * 

# Seed the same as the generator, to the minute
seed(int(time.time()) - int(time.time() % 60))
print(randint(0,100000000000)) # Contains the random lottery number!

```
