'''
In order to run this, install the following: 
- python3 
- flask 
- flask_cors 
- requests 

To run: 
- `python3 main.py`
'''

from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
import functionality 


app = Flask(__name__)
CORS(app) # Enable Access-Control-Allow-Origin

# Gets all links for a given username
@app.route("/get_link", methods=['GET'])
def get_link():
	username = request.args.get('username')
	result = functionality.get_link_info(username)
	return {'link' : result}

# Create a user. Returns a magic_link to be used for editing
@app.route("/create_user", methods=['POST'])
def create_user(): 
	username = request.json['username']
	result = functionality.create_user(username)
	if(result == False):
		return 'False'
	return result

# Get all link content associated with a user
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


# Given a link that stores text, send this text back to the user
@app.route("/get_text", methods=['GET'])
def get_text():

	link = request.args.get('link')
	username = request.args.get('username');
	text = functionality.get_text(link)	

	# If the flag is equal the data being returned
	flag_file = open("../../flag.txt")
	flag = flag_file.read()
	
	if(text == flag):
		functionality.delete_profile(username);
		text += " --- This profile will be removed in order to prevent the flag from being disclosed"
	return text


# Get all users currently in the system
@app.route("/get_users", methods=['GET'])
def get_users():

	# Get the users and reorganize them
	users = functionality.get_users()
	users_lst = []
	for user in users: 
		user = user[0]
		users_lst.append(user)
	
	# Send back a JSON list of users
	return jsonify(users=users_lst)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
