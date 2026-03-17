-- Task 7: Update One Student
-- Change age of student with id=1

USE school_db;

-- TODO: UPDATE students SET age = 16 WHERE id = 1;
-- Remember to use WHERE!
-- Update one column
UPDATE table_name
SET column1 = new_value
WHERE condition;
 
-- Update multiple columns
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;
 
-- Update with calculation
UPDATE table_name
SET column = column + 10
WHERE condition;