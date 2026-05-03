USE join_lab;

SELECT 
    a.name AS person_a, 
    b.name AS person_b, 
    a.dept_id
FROM staff a
JOIN staff b 
    ON a.dept_id = b.dept_id
    AND a.staff_id < b.staff_id;