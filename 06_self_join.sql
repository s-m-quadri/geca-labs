-- Task 6: Self join — pairs of staff in the **same** department (same dept_id)
-- Avoid duplicate pairs: only rows where a.staff_id < b.staff_id

USE join_lab;

-- TODO: SELECT a.name AS person_a, b.name AS person_b, a.dept_id
-- FROM staff a
-- JOIN staff b ON ...
SELECT a.name AS person_a, b.name AS person_b, a.dept_id
FROM staff a
JOIN staff b ON a.dept_id = b.dept_id AND a.staff_id < b.staff_id;