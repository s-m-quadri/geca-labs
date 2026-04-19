-- Task 7: Non-equi join — pairs of staff where person A joined **strictly before** person B (same department)

USE join_lab;

-- TODO: JOIN staff a to staff b on same dept_id AND a.joined_on < b.joined_on
-- Show a.name, b.name, a.joined_on, b.joined_on

select a.name as person_b,b.name as person_b,a.joined_on as person_a_joined_on,b.joined_on as person_b_joined_on
from staff a
join staff b
where a.dept_id=b.dept_id and a.joined_on<b.joined_on;