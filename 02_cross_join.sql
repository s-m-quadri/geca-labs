USE join_lab;

SELECT staff.name, projects.title
FROM staff
CROSS JOIN projects;