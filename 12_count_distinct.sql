-- Task 12: Count — COUNT(DISTINCT)
-- How many distinct departments appear?

USE school_db;

-- TODO: SELECT COUNT(DISTINCT dept) AS distinct_depts FROM employees;

-- Guidance: COUNT(DISTINCT column) counts unique non-NULL values in that column.
-- For departments, this will give the number of unique dept values in the employees table.
-- Remember, COUNT(*) counts all rows, while COUNT(column) counts non-NULL values in that column.
-- Check the manual for COUNT examples: https://www.s-m-quadri.me/geca/dbms/03 (count section).
-- After writing the query, run 15_check_status.sql to verify your progress.
-- What does DISTINCT do here? How does it differ from COUNT(dept) without DISTINCT?
