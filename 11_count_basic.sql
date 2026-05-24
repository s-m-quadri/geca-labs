-- Task 11: Count — COUNT(*)
-- Total rows and how many have salary >= 40000 (use SUM of a condition or subquery pattern).

USE school_db;

-- TODO: SELECT COUNT(*) AS total_employees FROM employees;
-- Hint: COUNT(*) counts all rows in the table, regardless of NULL values. What does it return for the employees table?

-- TODO: One query: count rows where salary >= 40000
-- Hint: SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
--   or COUNT with WHERE in a subquery
-- Remember, SUM with CASE can conditionally count rows. Alternatively, think about using a subquery with COUNT and WHERE.
-- Check the manual for COUNT examples: https://www.s-m-quadri.me/geca/dbms/03
-- Guiding question: How can you combine both counts in a single query?
-- After trying, run 15_check_status.sql to verify your inserts and groupings.
