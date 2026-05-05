USE join_lab;

-- Strategy:
-- 1) All projects (with or without staff)
-- 2) Add staff who are not in any project
-- 3) Combine using UNION

-- Part 1: Projects with staff (or NULL if no staff)
SELECT 
    p.title,
    s.name
FROM projects p
LEFT JOIN project_staff ps 
    ON p.proj_id = ps.proj_id
LEFT JOIN staff s 
    ON ps.staff_id = s.staff_id

UNION

-- Part 2: Staff with no project
SELECT 
    NULL AS title,
    s.name
FROM staff s
LEFT JOIN project_staff ps 
    ON s.staff_id = ps.staff_id
WHERE ps.proj_id IS NULL;