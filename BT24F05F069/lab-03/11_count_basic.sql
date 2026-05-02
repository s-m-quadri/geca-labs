USE school_db;

SELECT COUNT(*) AS total_employees FROM employees;

SELECT SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS high_earners
FROM employees;