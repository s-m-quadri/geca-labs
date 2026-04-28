-- Task 7: Non-equi join — pairs of staff where person A joined **strictly before** person B (same department)

USE join_lab;

-- TODO: JOIN staff a to staff b on same dept_id AND a.joined_on < b.joined_on
-- Show a.name, b.name, a.joined_on, b.joined_on

SELECT a.name AS person_a, b.name AS person_b, a.joined_on AS a_joined, b.joined_on AS b_joined
FROM staff a
JOIN staff b ON a.dept_id = b.dept_id AND a.joined_on < b.joined_on
ORDER BY a.dept_id, a.joined_on, b.joined_on;
