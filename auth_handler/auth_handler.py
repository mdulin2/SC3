'''
User Authentication...
Running: `python3 auth_hander.py`
Network setup: `socat TCP-LISTEN:6001,fork,reuseaddr EXEC:"python3 auth_handler.py"`

'''

# Create a user, with a specific auth level 
def create_user(user_amount):
	name = input("Name: ") 
	level = input("Level (1-5): ") 
	return [user_amount, name, int(level)]

# Get the uid of a user
def get_uid(): 

	# Default value	
	uid = 0
	try: 
		tmp_int = input("Please enter a valid UID (int): ") 
		# Prevent negative and root accounts
		if(int(tmp_int) == 0 or int(tmp_int) < 0): 
			print("Illegal UID") 
			return -1
		
		# Set the uid, if valid
		uid = tmp_int

	# In the case of a bad input
	except:	
		print("Illegal UID -- Invalid Chars") 	
	
	return int(uid)
	
# Login by the userid
def login(users): 

	# Use the get_uid in order to login to the user
	uid = int(get_uid())
	if(uid == -1): 
		print("Invalid User") 
		return -1 

	for uid_i in users: 
		# Check the uid of the user in order to login
		if(uid == uid_i[0]): 
			return uid_i[0]

	print("Invalid User...")
	return -1

# Create the default users
def initialize_users():
	user_lst = []
	user_lst.append([0,'admin', 10])
	return user_lst 

# Get the flag :) 
def get_flag(): 
	print("Flag!") 	

def main(): 
	user_lst = initialize_users()	

	index = 0
	logged_in_index = -1
	while(True):
		print("") 
		print("Options: ") 
		print("1. Create New User") 
		print("2. Login as User") 
		print("3. View Current User") 
		print("4. View All (level 5)") 
		print("5. Super Admin Feature (level 10)") 

		option = int(input("> "))

		# Create a new user		
		if(option == 1): 
			new_user = create_user(len(user_lst))
			user_lst.append(new_user)
			logged_in_index = new_user[0] 

		# Login as the user
		elif(option == 2):
			logged_in_index = login(user_lst)
			print("Logged in with the user") 

		# Print currrent user information
		elif(option == 3 and not logged_in_index == -1):
			print("\nUser Info: ") 
			print("Uid: " + str(user_lst[logged_in_index][0]))
			print("Name: ", str(user_lst[logged_in_index][1]))

		# Print all users
		elif(option == 4 and not logged_in_index == -1):
			if(user_lst[logged_in_index][2] < 5): 
				print("Need higher privs...")
				continue 

			print("\nAll Users: ") 
			for user in user_lst:
				print("--------------------------") 
				print("Uid: " + str(user[0]))
				print("Name: ", str(user[1]))
				print("Auth Level: ", str(user[2]))
				print("--------------------------") 

		# Print the flag, with only the proper auth creds (need auth level of 10 or higher
		elif(option == 5 and logged_in_index != -1 and user_lst[logged_in_index][2] >= 10): 
			get_flag()
			return 
		
		else: 
			print("Invalid Option...") 

main()

