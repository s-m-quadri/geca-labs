USE school_db;

SELECT dept, AVG(salary) AS avg_pay
FROM employees
GROUP BY dept
HAVING AVG(salary) > 35000;
SELECT dept,
  GROUP_CONCAT(full_name ORDER BY full_name SEPARATOR ', ') AS members
FROM employees
GROUP BY dept;