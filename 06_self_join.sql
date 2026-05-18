-- Task 6: Self join — pairs of staff in the **same** department (same dept_id)
-- Avoid duplicate pairs: only rows where a.staff_id < b.staff_id

<<<<<<< HEAD
USE join_lab;

 SELECT a.name AS person_a, b.name AS person_b, a.dept_id
FROM staff a
JOIN staff b ON a.dept_id = b.dept_id AND a.staff_id < b.staff_id
=======
SELECT a.name AS person_a, b.name AS person_b, a.dept_id
FROM staff AS a
JOIN staff AS b 
ON a.dept_id = b.dept_id 
AND a.staff_id < b.staff_id
ORDER BY a.dept_id, a.name, b.name;
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
