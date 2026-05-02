-- Task 1: Setup database and employees table
-- You need sample data for later tasks (at least 5 rows, 2+ departments).

-- TODO: DROP DATABASE IF EXISTS school_db; then CREATE DATABASE school_db;

-- TODO: USE school_db;

-- TODO: CREATE TABLE employees with:
--   emp_id INT PRIMARY KEY AUTO_INCREMENT
--   full_name VARCHAR(60) NOT NULL
--   dept VARCHAR(40)
--   salary DECIMAL(10,2)
--   hire_date DATE
--   phone VARCHAR(25)

-- TODO: INSERT at least 5 rows. Vary dept, salary, hire_date.
-- Optional: put leading/trailing spaces in some phone values for TRIM task later.

-- TODO: SELECT * FROM employees;

    CREATE DATABASE IF NOT EXISTS school_db;
    USE school_db;
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INT PRIMARY KEY AUTO_INCREMENT ,
        full_name VARCHAR(60) NOT NULL ,
        dept VARCHAR(40) ,
        salary DECIMAL(10,2) ,
        hire_date DATE ,
        phone VARCHAR(25) 
    );
    INSERT INTO employees (full_name , dept , salary , hire_date , phone) VALUES
    ('MAYANK SHARMA', 'cse' , 50000.0 , '2024-06-30', ' 123-456-7890 '),
    ('ANITA GUPTA', 'ece' , 55000.0 , '2023-05-15', '987-654-3210'),
    ('RAHUL VERMA', 'cse' , 60000.0 , '2022-04-10', ' 555-555-5555'),
    ('PRIYA SINGH', 'mech' , 45000.0 , '2021-03-20', '444-444-4444'),
    ('VIKRAM PATEL', 'ece' , 52000.0 , '2020-02-25', '333-333-3333');

    SELECT * FROM employees;

