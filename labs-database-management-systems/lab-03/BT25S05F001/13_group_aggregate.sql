USE school_db;

-- TODO: SELECT dept,
--   COUNT(*) AS n,
--   SUM(salary) AS total_pay,
--   AVG(salary) AS avg_pay
-- FROM employees
-- GROUP BY dept;

SELECT dept,
COUNT(*) AS n,
SUM(salary) AS total_pay,
AVG(salary) AS avg_pay
FROM employees
GROUP BY dept;