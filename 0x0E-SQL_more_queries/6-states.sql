-- Create the database hbtn_0d_usa and the table states with id INT AUTO_INCREMENT PRIMARY KEY and name VARCHAR(256) NOT NULL.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
