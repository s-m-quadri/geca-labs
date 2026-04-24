USE join_lab;

-- TODO: SELECT a.name AS person_a, b.name AS person_b, a.dept_id
-- FROM staff a
-- JOIN staff b ON ...

-- Hint: For a self-join, join the staff table to itself on the dept_id column to find pairs in the same department.
-- To avoid duplicate pairs and self-pairs, add a WHERE clause with a.staff_id < b.staff_id.
-- What does the ON clause look like? Sketch the join: staff a connects to staff b where their dept_id matches.
