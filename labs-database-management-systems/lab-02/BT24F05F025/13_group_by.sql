-- Task 13: Group By
-- Count students in each grade

USE school_db;
select grade, count(*) as count from students group by g

-- TODO: SELECT grade, COUNT(*) as count FROM students GROUP BY grade;
