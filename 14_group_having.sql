-- Task 14: Group — HAVING and GROUP_CONCAT (MySQL)
-- Part A: departments where average salary is strictly greater than 35000.
-- Part B: for each department, comma-separated list of names (ORDER BY full_name).

USE school_db;

-- TODO (Part A): SELECT dept, AVG(salary) AS avg_pay
-- FROM employees
-- GROUP BY dept
-- HAVING AVG(salary) > 35000;

-- TODO (Part B): SELECT dept,
--   GROUP_CONCAT(full_name ORDER BY full_name SEPARATOR ', ') AS members
-- FROM employees
-- GROUP BY dept;

-- select dept,AVG(salary) as avg_pay
-- from employees
-- GROUP BY dept
-- having AVG(salary) > 35000;

SELECT dept,
group_concat(full_name order by full_name separator ',') as members
from employees
group by dept;