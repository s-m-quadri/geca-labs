-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
-- Strategy: I will use a UNION of two LEFT JOINs. The first LEFT JOIN will get all staff and their projects, including those with no projects. The second LEFT JOIN will get all projects and their staff, including those with no staff. Then I will combine the results to get a full outer join effect.
select staff.name, projects.title
from staff
left join project_staff on staff.staff_id = project_staff.staff_id
left join projects on project_staff.project_id = projects.project_id
union
select staff.name, projects.title
from projects
left join project_staff on projects.project_id = project_staff.project_id
left join staff on project_staff.staff_id = staff.staff_id
order by staff.name, projects.title;        