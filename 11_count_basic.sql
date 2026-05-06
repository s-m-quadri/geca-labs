USE school_db;

-- Total employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- TODO: One query: count rows where salary >= 40000
-- Hint: SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
--   or COUNT with WHERE in a subquery

SELECT COUNT(*) AS total_employees FROM employees;

SELECT COUNT(salary)
    FROM employees
        WHERE salary>=40000;
