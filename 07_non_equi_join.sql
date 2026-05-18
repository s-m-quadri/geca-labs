<<<<<<< HEAD
-- Task 7: Non-equi join — pairs of staff where person A joined **strictly before** person B (same department)

USE join_lab;

 SELECT a.name AS person_a, b.name AS person_b, a.joined_on AS joined_on_a, b.joined_on AS joined_on_b
FROM staff a
JOIN staff b ON a.dept_id = b.dept_id AND a.joined_on < b.joined_on
-- Show a.name, b.name, a.joined_on, b.joined_on
=======
SELECT a.name , b.name , a.joined_on , b.joined_on
FROM staff AS a
JOIN staff AS b
ON a.dept_id = b.dept_id
AND a.joined_on < b.joined_on
ORDER BY a.dept_id, a.joined_on, b.joined_on, a.name, b.name;
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
