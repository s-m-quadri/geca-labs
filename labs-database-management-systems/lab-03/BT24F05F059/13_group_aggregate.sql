USE school_db;
SELECT dept,
       COUNT(*)      AS headcount,
       SUM(salary)   AS total_salary,
       AVG(salary)   AS avg_salary
FROM employees
GROUP BY dept;