USE join_lab;
SELECT a.name AS person_a, b.name AS person_b
FROM staff AS a
JOIN staff AS b
  ON a.dept_id = b.dept_id AND a.staff_id < b.staff_id;