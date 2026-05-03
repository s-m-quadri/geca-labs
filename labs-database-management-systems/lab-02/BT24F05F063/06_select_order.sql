-- Task 6: Select with ORDER BY
-- Show students sorted by age (oldest first)

USE school_db;

-- TODO: SELECT all students ORDER BY age DESC
SELECT name, age FROM students ORDER BY age DESC;
SELECT name , grade FROM students ORDER BY grade;