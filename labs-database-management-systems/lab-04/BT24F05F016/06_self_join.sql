-- Task 6: Self join — pairs of staff in the **same** department (same dept_id)
-- Avoid duplicate pairs: only rows where a.staff_id < b.staff_id

USE join_lab;

SELECT a.name AS person_a, b.name AS person_b, a.dept_id
FROM staff a
JOIN staff b ON a.dept_id = b.dept_id
WHERE a.staff_id < b.staff_id
ORDER BY a.dept_id, person_a, person_b;
