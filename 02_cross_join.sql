USE join_lab;
SELECT s.name AS staff_name, p.title AS project_title
FROM staff AS s
CROSS JOIN projects AS p;