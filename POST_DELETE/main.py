'''
In order to run this, install the following: 
- python3 
- flask 

To run: 
- `python3 main.py`
'''

from flask import Flask
from flask import request

app = Flask(__name__)

# Open the flag file
with open('flag.txt') as f:
	flag = f.read()
flg_1, flg_2 = flag[:int(len(flag)/2)], flag[int(len(flag)/2):] # Cut the string in half

@app.route("/route1", methods=['POST'])
def put():
	return flg_1 + '\n'

@app.route("/route2", methods=['DELETE'])
def patch(): 
	return flg_2 + '\n'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8084) 
