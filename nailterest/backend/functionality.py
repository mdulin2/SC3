import sqlite3
from os import urandom
import base64
import requests

conn = sqlite3.connect('storage.db', check_same_thread=False)
c = conn.cursor()

# Setup the database by creating the tables
def setup(): 

	create_users = '''
CREATE TABLE users (
username varchar(255), 
magic_link varchar(1023), 
PRIMARY KEY(username)
);

'''	

	create_link_storage = '''
CREATE TABLE links (
id int AUTO_INCREMENT,
username varchar(255), 
link_value varchar(1023), 
PRIMARY KEY(id),
FOREIGN KEY (username) REFERENCES users(username)
);

'''
	#c.execute(create_users)
	c.execute(create_link_storage)


''' 
Adds a user account 
name: The user to create 

Returns: 
	false (for error) or the magic_link for the user 
'''
def create_user(name):
	# Checks to see if the user already exists 
	# If so, return 
	# If not, create a magic long random link 
	# Return the magic link

	# Validate that the current user does not exist
	query = "SELECT * FROM users WHERE username=?"
	results = c.execute(query, (name,)) 
	results = results.fetchall()

	print(results)
	if(results != []): 
		return False

	# Generate the random link to be used for editing (secure random)
	encoded_bytes = base64.b64encode(urandom(100))
	magic_link = str(encoded_bytes, "utf-8")
	
	# Add the new user
	query = """INSERT INTO users(username, magic_link) VALUES(?,?)"""	
	results = c.execute(query, (name,magic_link))

	# TODO Figure out database connection stuff
	conn.commit()
	return magic_link


'''
Adds a link for a user 
user: username to add the link for 
link: the link to add for the user 

Returns: 
	Nothing

NOTE: This function assumes that the username exists
'''
def add_link(user,link):
	query = """INSERT INTO links(username, link_value) VALUES(?,?);"""
	results = c.execute(query, (user, link))
	conn.commit()
	return True	


'''
Get the link information for a given user
user: The username of to grab the information for.

Returns: 
	All the links for a particular user
'''
def get_link_info(user):

	# Validate that the user exists
	query = """SELECT * FROM users WHERE username = ?;"""
	results = c.execute(query, (user,))
	results = results.fetchall()
	if(results == []):
		return False

	# Get the links for a given user
	query = """SELECT link_value FROM links WHERE username = ?;"""
	results = c.execute(query, (user,))
	results = results.fetchall()
	return results


'''
Get the user associated with a magic link

magic_link: The link associated with a user

Returns: 
	- A list of users associated with a link
'''
def user_for_link(magic_link):

	query = """SELECT username FROM users WHERE magic_link = ?;"""
	results =  c.execute(query, (magic_link,))
	results = results.fetchall()
	return results 

'''
Retrieve the data from a text file online 

link: The link to grab data from

Return:
	String with the content of the link
'''
def get_text(link):
	response = requests.get(link)	
	data = response.text
	return data

def get_users(): 
	query = """SELECT username FROM users;"""
	results = c.execute(query)
	results = results.fetchall()
	return results

			
#setup()
#add_link("A", "https://github.com/mdulin2/Zyxel_NAS326_Exploit/blob/master/README.md")
#print(get_link_info("dad"))
#print(user_for_link("h2FPwZL1waMEupOjflQify1LSF/GJujMA7TY1JRgAd/rTQWgrdx1dXbbigcoX9WtSLKL5VR1UNTzBHr5OSsKadgMOTnzDsvWsVK3+b407TZ0XKGId1gfTHfKI3OoAa39lpgCtA=="))
print(get_users())
