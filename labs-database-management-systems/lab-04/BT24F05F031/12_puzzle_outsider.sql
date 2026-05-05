USE join_lab;

SELECT s.name, p.title
FROM project_staff ps
JOIN staff s      ON s.staff_id = ps.staff_id
JOIN projects p   ON p.project_id = ps.project_id
-- (optional, only if you want dept names)
-- JOIN departments sd ON sd.dept_id = s.dept_id
-- JOIN departments pd ON pd.dept_id = p.dept_id
WHERE s.dept_id <> p.dept_id;