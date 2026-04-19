USE join_lab;

SELECT 
    a.name AS person_a,
    b.name AS person_b,
    a.joined_on,
    b.joined_on
FROM staff a
JOIN staff b
    ON a.dept_id = b.dept_id
    AND a.joined_on < b.joined_on;