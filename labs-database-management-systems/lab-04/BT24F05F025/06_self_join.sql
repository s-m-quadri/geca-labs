-- Task 6: Self join — pairs of staff in the **same** department (same dept_id)
-- Avoid duplicate pairs: only rows where a.staff_id < b.staff_id

USE join_lab;
select a.name AS person_a, b.name AS person_b, a.dept_id
from staff a
join staff b on a.dept_id = b.dept_id and a.staff_id < b.staff_id
order by a.dept_id, a.name, b.name; 


-- TODO: SELECT a.name AS person_a, b.name AS person_b, a.dept_id
-- FROM staff a
-- JOIN staff b ON ...
