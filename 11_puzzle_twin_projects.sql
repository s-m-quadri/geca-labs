USE join_lab;

-- Puzzle A: Finding the one person booked on both "sibling" projects
SELECT s.name
FROM staff s
JOIN project_staff ps1 ON s.staff_id = ps1.staff_id
JOIN project_staff ps2 ON s.staff_id = ps2.staff_id
JOIN projects p1 ON ps1.proj_id = p1.proj_id
JOIN projects p2 ON ps2.proj_id = p2.proj_id
WHERE p1.dept_id = p2.dept_id  -- Same home department
  AND p1.proj_id < p2.proj_id; -- Different projects (prevents duplicates)