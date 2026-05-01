-- Task 4: Left outer join — all departments, even if no staff

USE join_lab;

-- TODO: SELECT departments.dept_name, staff.name
-- FROM departments
-- LEFT JOIN staff ON staff.dept_id = departments.dept_id
-- ORDER BY departments.dept_id, staff.name;
<<<<<<< HEAD
SELECT departments.dept_name, staff.name
FROM departments
LEFT JOIN staff
ON staff.dept_id = departments.dept_id
ORDER BY departments.dept_id, staff.name;
=======
USE join_lab;
SELECT d.dept_name, s.name AS staff_name
FROM departments AS d
LEFT JOIN staff AS s ON d.dept_id = s.dept_id;
>>>>>>> e2f4f0375b403b79b5fcba93999f68f26d20175a
