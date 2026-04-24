-- Task 13: Group — SUM and AVG by department
-- For each dept: employee count, total salary, average salary.

USE school_db;

-- TODO: SELECT dept,
--   COUNT(*) AS n,
--   SUM(salary) AS total_pay,
--   AVG(salary) AS avg_pay
-- FROM employees
-- GROUP BY dept;

-- Hint: To group data by department and calculate aggregates like count, sum, and average, 
-- remember that GROUP BY organizes rows into groups based on the specified column(s). 
-- Aggregate functions like COUNT(*), SUM(), and AVG() operate on each group. 
-- Ensure all non-aggregated columns in SELECT are included in GROUP BY to avoid errors (depending on your MySQL sql_mode).
-- Check the manual for GROUP BY examples: https://www.s-m-quadri.me/geca/dbms/03
-- What happens if you uncomment and run this query? Does it work with your current data?
-- After trying, run 15_check_status.sql to verify your progress.
