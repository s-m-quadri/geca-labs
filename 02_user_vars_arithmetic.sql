-- Task 2: Arithmetic in a SELECT (+ - * /)
-- PostgreSQL has no session variables (@a := ...); just SELECT the expressions.
\c proc_lab

-- TODO: SELECT 17 + 5 AS sum_, 17 - 5 AS diff, 17 * 5 AS prod, 17.0 / 5 AS quot;
-- Connect to the database
\c proc_lab

-- Perform basic arithmetic operations
SELECT 
    17 + 5 AS sum_, 
    17 - 5 AS diff, 
    17 * 5 AS prod, 
    17.0 / 5 AS quot;