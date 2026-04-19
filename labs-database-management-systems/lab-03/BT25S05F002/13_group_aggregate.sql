-- Task 13: Group — SUM and AVG by department
-- For each dept: employee count, total salary, average salary.

USE school_db;

-- TODO: SELECT dept,
--   COUNT(*) AS n,
--   SUM(salary) AS total_pay,
--   AVG(salary) AS avg_pay
-- FROM employees
-- GROUP BY dept;

select dept,
count(*)as n,
sum(salary) as total_pay,
avg(salary) as avg_pay
from employees
group by dept;