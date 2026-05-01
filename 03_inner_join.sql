-- Task 3: Inner join — staff with their department name

USE join_lab;

<<<<<<< HEAD
 SELECT staff.name, departments.dept_name
 FROM staff
 INNER JOIN departments ON staff.dept_id = departments.dept_id;
=======
SELECT staff.name, departments.dept_name
FROM staff
INNER JOIN departments ON staff.dept_id = departments.dept_id;
>>>>>>> c5bc72027f82f845608c3256226d1211c296effc
