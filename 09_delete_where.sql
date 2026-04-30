USE school_db;

-- Step 1: See who will be deleted
SELECT * FROM students
WHERE age < 15;

-- Step 2: Delete students younger than 15
DELETE FROM students
WHERE age < 15;

-- Step 3: Verify remaining records
SELECT * FROM students;
