USE join_lab;

-- Strategy:
-- 1. LEFT JOIN: all projects + matching staff (includes projects with no staff)
-- 2. RIGHT JOIN: all staff + matching projects (includes staff with no projects)
-- 3. UNION removes duplicates and gives full outer join behavior

SELECT 
    s.name AS staff_name,
    p.title AS project_title,
    ps.hours
FROM project_staff ps
LEFT JOIN staff s 
    ON ps.staff_id = s.staff_id
LEFT JOIN projects p 
    ON ps.proj_id = p.proj_id

UNION

SELECT 
    s.name AS staff_name,
    p.title AS project_title,
    ps.hours
FROM project_staff ps
RIGHT JOIN staff s 
    ON ps.staff_id = s.staff_id
RIGHT JOIN projects p 
    ON ps.proj_id = p.proj_id;