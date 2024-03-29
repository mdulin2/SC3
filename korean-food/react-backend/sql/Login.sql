USE injection;

DROP TABLE IF EXISTS Login;
DROP TABLE IF EXISTS Sessions;

CREATE TABLE Login(
    username    VARCHAR(200) NOT NULL,
    password    VARCHAR(200), 
    is_admin BOOLEAN NOT NULL
); 

charset utf8 collate utf8_general_ci; 

-- admin - Quinoa&Barley
INSERT INTO Login(username, password, is_admin) VALUES
    ('admin','gG9I2mb/58Ew3ONyqy91Q1W9663H21VT9SDfIeF+Pzo=', true);

CREATE TABLE Sessions(
	ID int NOT NULL AUTO_INCREMENT,
	username  VARCHAR(200) NOT NULL,
    	session    VARCHAR(200) NOT NULL,
    PRIMARY KEY(ID)
);
