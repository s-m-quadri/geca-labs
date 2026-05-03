-- Task 4: Left outer join — all departments, even if no staff

USE join_lab;

-- TODO: SELECT departments.dept_name, staff.name
-- FROM departments
-- LEFT JOIN staff ON staff.dept_id = departments.dept_id
-- ORDER BY departments.dept_id, staff.name;
 select departments.dept_name,staff.name from departments left join staff on staff.dept_id = departments.dept_id order by departments.dept_id,staff.name;
 SELECT 
    p.proj_id,
    p.title AS project_title,
    s.staff_id,
    s.name AS staff_name,
    ps.hours
FROM 
    projects p
LEFT JOIN 
    project_staff ps
ON 
    p.proj_id = ps.proj_id
LEFT JOIN 
    staff s
ON 
    ps.staff_id = s.staff_id;