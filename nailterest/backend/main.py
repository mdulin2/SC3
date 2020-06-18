'''
In order to run this, install the following: 
- python3 
- flask 

To run: 
- `python3 main.py`
'''

from flask import Flask
from flask import request
import functionality 


app = Flask(__name__)


@app.route("/get_link", methods=['GET'])
def get_link():
	username = request.args.get('username')
	result = functionality.get_link_info(username)
	return {'link' : result}

@app.route("/create_user", methods=['POST'])
def create_user(): 
	username = request.json['username']
	result = functionality.create_user(username)
	if(result == False):
		return 'False'
	return result

@app.route("/add_link", methods=['POST'])
def add_link(): 

	# Get the user for a given link
	magic_link = request.json['magic_link']
	link = request.json['link']
	name = functionality.user_for_link(magic_link)
	if(name == []):
		return 'False'

	functionality.add_link(name[0][0], link)	
		
	return 'True'

@app.route("/get_text", methods=['GET'])
def get_text():
	link = request.args.get('link')
	text = functionality.get_text(link)	
	return text

if __name__ == "__main__":
    app.run(debug=True)
