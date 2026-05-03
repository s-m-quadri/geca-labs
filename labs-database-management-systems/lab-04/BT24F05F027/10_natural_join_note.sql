USE join_lab;

SELECT 
    p.title, 
    d.dept_name, 
    d.floor_no
FROM projects p
INNER JOIN departments d 
    ON p.dept_id = d.dept_id;