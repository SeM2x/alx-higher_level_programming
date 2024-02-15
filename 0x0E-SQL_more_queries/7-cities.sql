-- Creates the database hbtn_0d_usa and the table cities
-- (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id AUTO_INCREMENT PRIMARY KEY,
	state_id INT FOREIGN KEY REFERENCES hbtn_0d_usa.states(id) NOT NULL,
	name VARCHAR(256)
);
