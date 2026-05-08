USE school_db;
-- Part A
SELECT dept, AVG(salary) AS avg_sal
FROM employees
GROUP BY dept
HAVING AVG(salary) > 35000;
 
-- Part B
SELECT dept, GROUP_CONCAT(full_name ORDER BY full_name SEPARATOR ', ') AS members
FROM employees
GROUP BY dept;