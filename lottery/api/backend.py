from flask import Flask
from redis import Redis
#from numpy.random import randint
from flask_cors import CORS
from random import * 
import time

from apscheduler.schedulers.background import BackgroundScheduler 

app = Flask(__name__)
CORS(app)
sched = BackgroundScheduler(daemon=True) # Scheduler object 

# app.config['CORS_HEADERS'] = 'Content-Type'
redis = Redis(host='redis', port=6379, charset="utf-8", decode_responses=True)

def fetch_data_from_api(): 
    print("Generating new number...")
    # Seed the random number generator
    seed(int(time.time()))

    number = randint(0, 100000000000) 
    redis.lpush('history', number)
 
#add your job here 
sched.add_job(fetch_data_from_api, 'cron', minute='*')
sched.start() 

@app.route('/')
def start():
    redis.incr('hits')
    return '{} times.'.format(redis.get('hits'))

@app.route('/register/<name>')
def register(name):
    redis.mset({name: 0})
    return 'User registered with name: {}'.format(name)

@app.route('/guess/<name>/<number>')
def guess(name, number):
    redis.mset({name: number})
    return 'User {} guessed: {}'.format(name, redis.get(name))

@app.route('/validate/<name>')
def validate(name):
    guessed = int(redis.get(name))
    if (int(redis.lindex('history', 0)) == guessed):
        
        contents = ""
        with open('flag.txt') as f:
            contents = f.read()
        return 'You guessed right! Your size is: {}'.format(contents)
    return 'Wrong guess'

@app.route('/history')
def history():
    return {'History': redis.lrange('history', 2, -1)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
