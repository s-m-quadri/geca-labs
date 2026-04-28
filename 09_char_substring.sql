-- Task 9: Character — SUBSTRING, LEFT, LENGTH
-- First three letters of name; length of full_name.

USE school_db;

SELECT full_name,
  LEFT(full_name, 3) AS prefix3,
  SUBSTRING(full_name, 1, 3) AS sub3,
  LENGTH(full_name) AS name_len
FROM employees;
