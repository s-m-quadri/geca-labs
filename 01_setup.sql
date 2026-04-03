-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

DROP DATABASE IF EXISTS school_db;
CREATE DATABASE school_db;

USE school_db;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(60) NOT NULL,
    dept VARCHAR(40),
    salary DECIMAL(10,2),
    hire_date DATE,
    phone VARCHAR(25)
);

INSERT INTO employees (full_name, dept, salary, hire_date, phone)
VALUES
("Adarsh Singh","CSE",6000.69,'2026-03-27'," 9696523210 "),
("Ash Ketchum","IT",12000,'2025-01-01',"1254786741"),
("Shreya Singh","ELE",40000,'2026-02-28',"9011602241"),
("Zoro Juro","ENTC",150,'2000-03-27',"5461237890"),
("Nami Chan","Civil",120009,'2026-03-17',"4568523790"),
("Monkey D Luffy","Mech",0.69,'2000-03-27',"4521496351");

SELECT * FROM employees;