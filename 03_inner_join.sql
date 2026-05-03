-- Task 3: Inner join — staff with their department name

USE join_lab;

-- TODO: SELECT staff.name, departments.dept_name
-- FROM staff
-- INNER JOIN departments ON staff.dept_id = departments.dept_id;
USE join_lab;

-- Match staff members to their respective department names
SELECT 
    staff.name, 
    departments.dept_name
FROM staff
INNER JOIN departments 
    ON staff.dept_id = departments.dept_id;
    