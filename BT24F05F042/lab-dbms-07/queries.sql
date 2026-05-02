-- 1. All students
SELECT * FROM students;

-- 2. Students with their courses (JOIN)
SELECT s.name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 3. Count students per course (GROUP BY)
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- 4. Students with grade A
SELECT s.name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.grade = 'A';

-- 5. Courses taught by CS faculty
SELECT c.course_name
FROM courses c
JOIN faculty f ON c.faculty_id = f.faculty_id
WHERE f.department = 'CS';

-- 6. Students enrolled in more than 1 course
SELECT student_id
FROM enrollments
GROUP BY student_id
HAVING COUNT(course_id) > 1;

-- 7. Subquery: students in DBMS
SELECT name FROM students
WHERE student_id IN (
  SELECT student_id FROM enrollments
  WHERE course_id = 201
);

-- 8. View example
CREATE VIEW student_courses AS
SELECT s.name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

SELECT * FROM student_courses;
-- 9. Highest grade per course (extra query)
SELECT 
  course_id, 
  MAX(grade) AS highest_grade
FROM enrollments
GROUP BY course_id;