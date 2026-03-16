-- Task 6: Select with ORDER BY
-- Show students sorted by age (oldest first)

USE school_db;

-- TODO: SELECT all students ORDER BY age DESC
-- Sort by age (youngest first)
SELECT * FROM students ORDER BY age ASC;
 
-- Sort by age (oldest first)
SELECT * FROM students ORDER BY age DESC;
 
-- Sort by name alphabetically
SELECT * FROM students ORDER BY name ASC;