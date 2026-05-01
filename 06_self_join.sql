-- Task 6: Self join — pairs of staff in the **same** department (same dept_id)
-- Avoid duplicate pairs: only rows where a.staff_id < b.staff_id

USE join_lab;

-- TODO: SELECT a.name AS person_a, b.name AS person_b, a.dept_id
-- FROM staff a
-- JOIN staff b ON ...
<<<<<<< HEAD
SELECT a.name AS person_a,
       b.name AS person_b,
       a.dept_id
FROM staff a
JOIN staff b
ON a.dept_id = b.dept_id
AND a.staff_id < b.staff_id;
=======
USE join_lab;
SELECT a.name AS person_a, b.name AS person_b
FROM staff AS a
JOIN staff AS b
  ON a.dept_id = b.dept_id AND a.staff_id < b.staff_id;
>>>>>>> e2f4f0375b403b79b5fcba93999f68f26d20175a
