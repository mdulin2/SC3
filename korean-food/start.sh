#!/bin/bash 

# Backend startup 
tmux new-session -d -s "backend" "cd /application/react-backend && npm start" 

# React frontend startup
tmux new-session -d -s "frontend" "cd /application/client && yarn start" 

# Startup and initialize mysql 
service mysql start
mysqld_safe --skip-grant-tables
mysql -u root -e "create database injection" # Create the main database
mysql -u root < /application/react-backend/sql/Login.sql # Initialize the users
mysql -u root < /application/react-backend/sql/KoreanFood.sql # Initialize the food
mysql -u root -e "FLUSH PRIVILEGES;  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ChoosePassword'; FLUSH PRIVILEGES;" # Set a password again

sleep 1000000