-- Task 14: Group — HAVING and GROUP_CONCAT (MySQL)
-- Part A: departments where average salary is strictly greater than 35000.
-- Part B: for each department, comma-separated list of names (ORDER BY full_name).

USE school_db;

SELECT dept, AVG(salary) AS avg_pay
FROM employees
GROUP BY dept
HAVING AVG(salary) > 35000;

SELECT dept,
  GROUP_CONCAT(full_name ORDER BY full_name SEPARATOR ', ') AS members
FROM employees
GROUP BY dept;
