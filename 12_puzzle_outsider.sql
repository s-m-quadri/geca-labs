USE join_lab;

-- TODO: SELECT name, title (or equivalent) — rows for every such outsider
SELECT 
    s.name AS outsider_name, 
    p.title AS project_title
FROM staff s
JOIN project_staff ps ON s.staff_id = ps.staff_id
JOIN projects p ON ps.proj_id = p.proj_id  -- Fix: Change project_id to proj_id
WHERE s.dept_id <> p.dept_id;