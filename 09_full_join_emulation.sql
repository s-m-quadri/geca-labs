-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
write a query that uses a LEFT JOIN to get all project titles and staff names with hours, then UNION it with a query that gets all project titles with no staff assigned (using a LEFT JOIN and filtering for NULLs), and another query that gets all staff names with no projects assigned (using a LEFT JOIN and filtering for NULLs).
select projects.title, staff.name, project_staff.hours
from project_staff
join staff on project_staff.staff_id = staff.staff_id
join projects on project_staff.project_id = projects.project_id
union
select projects.title, null as name, null as hours
from projects
left join project_staff on projects.project_id = project_staff.project_id   
where project_staff.project_id is null
union
select null as title, staff.name, null as hours 
from staff
left join project_staff on staff.staff_id = project_staff.staff_id
where project_staff.staff_id is null
order by title, name;
                    