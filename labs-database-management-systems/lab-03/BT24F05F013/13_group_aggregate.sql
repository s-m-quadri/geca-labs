-- Task 13: Group — SUM and AVG by department
-- For each dept: employee count, total salary, average salary.

USE school_db;

-- TODO: SELECT dept,
--   COUNT(*) AS n,
--   SUM(salary) AS total_pay,
--   AVG(salary) AS avg_pay
-- FROM employees
-- GROUP BY dept;
USE school_db;

-- Department-wise summary
SELECT dept,
       COUNT(*) AS n,
       SUM(salary) AS total_pay,
       AVG(salary) AS avg_pay
FROM employees
GROUP BY dept;