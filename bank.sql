-- Bank Management System Database Setup
-- CBSE Class 12 Computer Science Project
-- Execute this script in MySQL to create the database and table

-- Create database
CREATE DATABASE IF NOT EXISTS bank;

-- Use the database
USE bank;

-- Create accounts table
CREATE TABLE IF NOT EXISTS accounts (
    acc_no INT PRIMARY KEY,
    name VARCHAR(50),
    dob DATE,
    address VARCHAR(100),
    phone VARCHAR(15),
    balance FLOAT
);

-- Display confirmation
SELECT 'Database and table created successfully!' AS Status;

