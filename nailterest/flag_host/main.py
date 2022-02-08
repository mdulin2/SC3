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
def get_flag_txt():
	flag_file = open("../flag.txt")
	flag = flag_file.read()
	return flag

@app.route("/flag.md", methods=['GET'])
def get_flag_md():
	flag_file = open("../flag.txt")
	flag = flag_file.read()
	return flag

@app.errorhandler(404)
def page_not_found(e):
    return "Internal Resources found on LAN! 404! Use /flag.md or /flag.txt for the URL"

if __name__ == "__main__":
    app.run(debug=True, port = 1337)
