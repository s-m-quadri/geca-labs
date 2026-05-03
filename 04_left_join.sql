-- Task 4: Left outer join — all departments, even if no staff

USE join_lab;

-- TODO: SELECT departments.dept_name, staff.name
-- FROM departments
-- LEFT JOIN staff ON staff.dept_id = departments.dept_id
-- ORDER BY departments.dept_id, staff.name;
USE join_lab;

-- List all departments and any staff assigned to them
SELECT 
    departments.dept_name, 
    staff.name AS staff_name
FROM departments
LEFT JOIN staff 
    ON departments.dept_id = staff.dept_id
ORDER BY departments.dept_id, staff.name;