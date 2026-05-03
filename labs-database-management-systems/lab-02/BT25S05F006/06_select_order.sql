-- Task 6: Select with ORDER BY
-- Show students sorted by age (oldest first)

USE school_db1;

-- TODO: SELECT all students ORDER BY age DESC
select * from students order by marks;
select id,name,marks from students order by marks;