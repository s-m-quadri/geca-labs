-- Task 2: Arithmetic in a SELECT (+ - * /)
-- PostgreSQL has no session variables (@a := ...); just SELECT the expressions.
\c proc_lab

-- TODO: SELECT 17 + 5 AS sum_, 17 - 5 AS diff, 17 * 5 AS prod, 17.0 / 5 AS quot;
select 17 + 5 as sum_, 17 - 5 as diff, 17 * 5 as prod, 17.0 / 5 as quot;                                       
