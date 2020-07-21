from flask import Flask, jsonify, request, session, make_response, render_template, url_for
from functools import wraps
import jwt
import datetime

app = Flask(__name__, static_folder=None)
app.config['SECRET_KEY'] = 'secret'


def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token = session['jwt']
        if not token:
            return jsonify({'message': 'Missing token. Have you logged in yet?'}), 403
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return wrapped

@app.route('/')
def index():
    links = []
    for rule in app.url_map.iter_rules():
        url = url_for(rule.endpoint, **(rule.defaults or {}))
        links.append((url, rule.endpoint))
    return render_template("index.html", links=links)

@app.route('/public')
def public():
        return 'Anyone can view this!'

@app.route('/private')
@check_for_token
def private():
    return 'flg{I\'m_in}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['logged_in'] = True
        token = jwt.encode({
            'user': 'User',
            'flag': 'flg{congratulations}',
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
            },
            app.config['SECRET_KEY'])
        session['jwt'] = token
        return jsonify({'token': token.decode('utf-8')})
    else:
        return render_template('login.html')
        #return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm="Login Required"'})

@app.route('/test')
@check_for_token
def test():
    return render_template('test.html')

@app.route('/admin')
@check_for_token
def admin():
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
    except:
        return jsonify({'message': 'Invalid token'}), 403
    if data['user'] == 'admin':
        return 'flg{sudo_gimme_access}'
    else:
        return jsonify({'message': 'Only the admin can see this page! >:V'}), 403


if __name__ == '__main__':
    app.run(debug=True)
