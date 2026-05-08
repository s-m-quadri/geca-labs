USE join_lab;
SELECT a.name AS earlier, b.name AS later
FROM staff AS a
JOIN staff AS b
  ON a.dept_id = b.dept_id AND a.joined_on < b.joined_on;