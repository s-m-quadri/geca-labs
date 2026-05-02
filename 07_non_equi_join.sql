-- Task 7: Non-equi join — pairs of staff where person A joined **strictly before** person B (same department)

USE join_lab;

-- TODO: JOIN staff a to staff b on same dept_id AND a.joined_on < b.joined_on
-- Show a.name, b.name, a.joined_on, b.joined_on

SELECT d.dept_name, s.name AS staff_name
FROM departments AS d
LEFT JOIN staff AS s ON d.dept_id = s.dept_id;