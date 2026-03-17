-- Task 14: Having Clause
-- Show grades that have more than 1 student

USE school_db1;

-- TODO: SELECT grade, COUNT(*) as count
-- FROM students
-- GROUP BY grade
-- HAVING count > 1;
select grade,COUNT(*) AS COUNT
from students group by grade
having count>=2;