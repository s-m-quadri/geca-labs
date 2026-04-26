-- Task 1: Setup Database and Table
-- Create database and students table

-- TODO: Create database school_db

-- TODO: Switch to school_db

-- TODO: Create students table with:
-- id INT PRIMARY KEY AUTO_INCREMENT
-- name VARCHAR(50)
-- age INT
-- grade VARCHAR(10)

create database school_db;
use school_db;
create table students (
    id int primary key auto_increment,
    name varchar(50),
    age int,
    grade varchar(10)
);