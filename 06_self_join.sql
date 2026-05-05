USE join_lab;

-- Task 6: Self join — pairs of staff in the same department
SELECT a.name AS person_a, b.name AS person_b, a.dept_id
FROM staff a
JOIN staff b ON a.dept_id = b.dept_id
WHERE a.staff_id < b.staff_id;