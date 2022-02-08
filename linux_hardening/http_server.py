#! /usr/bin/env python3
from flask.app import Flask
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__, )
app.config['SECRET_KEY'] = 'f2b93f898hc0i2h3c[0i32[kntrk'
auth = HTTPDigestAuth()

users = {
    "jeff": "i_like_c0ff33_2022",
}

@auth.get_password
def get_pw(username):
    return users.get(username)

@app.route('/')
@auth.login_required
def index():
    f = open("key.txt", "r")
    key = f.read()
    f.close()
    return f"Hello, {auth.username()}! Your key is <b>{key}</b>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
