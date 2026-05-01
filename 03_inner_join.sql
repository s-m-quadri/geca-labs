-- Task 3: Inner join — staff with their department name

USE join_lab;

-- TODO: SELECT staff.name, departments.dept_name
-- FROM staff
-- INNER JOIN departments ON staff.dept_id = departments.dept_id;
<<<<<<< HEAD
SELECT staff.name, departments.dept_name
FROM staff
INNER JOIN departments
ON staff.dept_id = departments.dept_id;
=======
USE join_lab;
SELECT s.name, d.dept_name
FROM staff AS s
INNER JOIN departments AS d ON s.dept_id = d.dept_id;
>>>>>>> e2f4f0375b403b79b5fcba93999f68f26d20175a
