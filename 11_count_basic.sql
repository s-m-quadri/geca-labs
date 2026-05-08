USE school_db;
SELECT COUNT(*) AS total,
       SUM(CASE WHEN salary >= 40000 THEN 1 ELSE 0 END) AS above_40k
FROM employees;