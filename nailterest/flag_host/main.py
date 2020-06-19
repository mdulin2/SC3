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
	return "flg{xyz}"

if __name__ == "__main__":
    app.run(debug=True, port = 8080)
