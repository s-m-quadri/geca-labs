USE school_db;

-- Part A: Avg salary > 35000
SELECT dept, AVG(salary) AS avg_pay
FROM employees
GROUP BY dept
HAVING AVG(salary) > 35000;

-- Part B: Names list per department
SELECT dept,
       GROUP_CONCAT(full_name ORDER BY full_name SEPARATOR ', ') AS members
FROM employees
GROUP BY dept;