-- Task 9: Character — SUBSTRING, LEFT, LENGTH
-- First three letters of name; length of full_name.

USE school_db;

-- TODO: SELECT full_name,
--   LEFT(full_name, 3) AS prefix3,
--   SUBSTRING(full_name, 1, 3) AS sub3,
--   LENGTH(full_name) AS name_len
-- FROM employees;

select full_name,
left(full_name,3) as prefix3,
left(full_name,4) as prefix4,
substring(full_name,1,3) as sub3,
substring(full_name,1,5) as sub5,
length(full_name) as name_len
from employees;