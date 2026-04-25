-- Task 4: Left outer join — all departments, even if no staff

USE join_lab;

-- TODO: SELECT departments.dept_name, staff.name
-- FROM departments
-- LEFT JOIN staff ON staff.dept_id = departments.dept_id
-- ORDER BY departments.dept_id, staff.name;
SELECT d.dept_name, s.name
FROM departments d
LEFT JOIN staff s
ON s.dept_id = d.dept_id
ORDER BY d.dept_id, s.name;                                              