USE join_lab;

-- Puzzle B: Finding the "Outsider"
SELECT 
    staff.name, 
    projects.title AS project_title
FROM staff
JOIN project_staff ON staff.staff_id = project_staff.staff_id
JOIN projects ON project_staff.proj_id = projects.proj_id
WHERE staff.dept_id <> projects.dept_id;
