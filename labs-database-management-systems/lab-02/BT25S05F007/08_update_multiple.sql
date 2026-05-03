USE school_db;

-- Update grade for all 10th graders
UPDATE students
SET grade = '10th-A'
WHERE grade = '10th';