-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy

select p.title as project_title,s.name as staff_name,ps.hours
from projects p
left join project_staff ps on ps.proj_id=p.proj_id
left join staff s on s.staff_id=ps.staff_id
union
select p.title as project_title,s.name as staff_name,ps.hours
from staff s
left join project_staff ps on ps.staff_id=s.staff_id
left join projects p on p.proj_id=ps.proj_id
where ps.proj_id=p.proj_id;

