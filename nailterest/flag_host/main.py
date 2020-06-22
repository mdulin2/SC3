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

@app.route("/flag.txt", methods=['GET'])
def get_flag():
	flag_file = open("../flag.txt")
	flag = flag_file.read()
	return flag

if __name__ == "__main__":
    app.run(debug=True, port = 8080)
