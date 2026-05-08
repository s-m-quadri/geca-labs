USE school_db;
SELECT full_name,
       YEAR(hire_date)  AS yr,
       MONTH(hire_date) AS mo,
       DAY(hire_date)   AS dy
FROM employees;