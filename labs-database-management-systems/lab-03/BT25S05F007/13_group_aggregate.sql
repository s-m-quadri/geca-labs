USE school_db;

-- Department-wise aggregation
SELECT 
    dept,
    COUNT(*) AS n,
    SUM(salary) AS total_pay,
    AVG(salary) AS avg_pay
FROM employees
GROUP BY dept;
