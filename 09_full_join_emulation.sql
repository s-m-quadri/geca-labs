-- Task 9: Full outer join emulation (MySQL has no FULL OUTER JOIN)
-- List every project title and every staff name that has hours on that project;
-- also show projects with no assignments and staff who never appear in project_staff (use UNION of left + anti patterns, or two LEFT JOINs with UNION — choose a correct emulation you can explain)

USE join_lab;

-- TODO: Write a query your instructor can run; add a short comment on your strategy
To emulate a full outer join in MySQL (which lacks native support), think about combining results from two LEFT JOINs using UNION. Start by sketching the tables on paper: projects linked to project_staff via proj_id, and staff linked to project_staff via staff_id.

- First, perform a LEFT JOIN from projects to project_staff, then to staff, to get all projects (including those with no staff assignments).
- Second, perform a LEFT JOIN from staff to project_staff, then to projects, but add a WHERE clause to filter only rows where the project side is NULL (i.e., staff with no project assignments).

What does "missing on the left" vs. "missing on the right" mean in this context? How would you ensure no duplicates in the UNION? Try writing the two SELECTs separately first, then combine them. If stuck, run `14_check_status.sql` to verify the seed data.