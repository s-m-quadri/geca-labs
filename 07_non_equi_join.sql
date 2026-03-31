SELECT a.name , b.name , a.joined_on , b.joined_on
FROM staff AS a
JOIN staff AS b
ON a.dept_id = b.dept_id
AND a.joined_on < b.joined_on
ORDER BY a.dept_id, a.joined_on, b.joined_on, a.name, b.name;
