-- Task 7: Non-equi join — pairs of staff where person A joined **strictly before** person B (same department)

USE join_lab;

-- TODO: JOIN staff a to staff b on same dept_id AND a.joined_on < b.joined_on
-- Show a.name, b.name, a.joined_on, b.joined_on
USE join_lab;
SELECT a.name AS person_a, b.name AS person_b, a.join_date AS a_join_date, b.join_date AS b_join_date
FROM staff a
JOIN staff b ON a.dept_id = b.dept_id AND a.join_date < b.join_date;''