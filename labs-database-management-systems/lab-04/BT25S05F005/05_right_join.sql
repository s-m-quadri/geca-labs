USE join_lab;

-- Task 5: Right outer join
-- Every staff member appears, with their department name if it exists.
SELECT departments.dept_name, staff.name
FROM departments
RIGHT JOIN staff ON staff.dept_id = departments.dept_id;