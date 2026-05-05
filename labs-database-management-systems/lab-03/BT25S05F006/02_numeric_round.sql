-- Task 2: Numeric — ROUND
-- Show each employee's salary rounded to whole rupees and to two decimals.

USE school_db1;

-- TODO: SELECT full_name, salary,
--   ROUND(salary, 0) AS salary_whole,
--   ROUND(salary, 2) AS salary_two_dec
-- FROM employees;
-- select full_name,salary from Employees;
 ROUND(salary,0) AS salary_whole,
    ROUND(salary,4) AS salary_two_dec;