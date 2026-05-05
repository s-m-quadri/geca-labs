-- Task 13: Group By
-- Count students in each grade

USE school_db1;

-- TODO: SELECT grade, COUNT(*) as count FROM students GROUP BY grade;
select grade,count(*) as count from students Group by grade;