-- Create Database
DROP DATABASE IF EXISTS library_db;
CREATE DATABASE library_db;
\c library_db;

-- Members Table
CREATE TABLE members (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Books Table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(150),
    author VARCHAR(100),
    available BOOLEAN DEFAULT TRUE
);

-- Staff Table
CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Borrow Table (Relationship)
CREATE TABLE borrow (
    borrow_id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(member_id),
    book_id INT REFERENCES books(book_id),
    staff_id INT REFERENCES staff(staff_id),
    borrow_date DATE,
    return_date DATE
);