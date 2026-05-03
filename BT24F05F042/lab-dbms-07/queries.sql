-- 1. Display all students
SELECT * FROM students;

-- 2. Display students with their enrolled courses (JOIN)
SELECT s.name AS student_name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 3. Count number of students per course (GROUP BY)
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- 4. Students who scored grade 'A'
SELECT s.name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.grade = 'A';

-- 5. Courses taught by faculty from CS department
SELECT c.course_name
FROM courses c
JOIN faculty f ON c.faculty_id = f.faculty_id
WHERE f.department = 'CS';

-- 6. Students enrolled in more than one course (GROUP BY + HAVING)
SELECT student_id, COUNT(course_id) AS course_count
FROM enrollments
GROUP BY student_id
HAVING COUNT(course_id) > 1;

-- 7. Subquery: Students enrolled in DBMS course (dynamic)
SELECT name 
FROM students
WHERE student_id IN (
  SELECT e.student_id
  FROM enrollments e
  JOIN courses c ON e.course_id = c.course_id
  WHERE c.course_name = 'DBMS'
);

-- 8. Create a VIEW for student-course mapping
CREATE OR REPLACE VIEW student_courses AS
SELECT s.name AS student_name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- View usage
SELECT * FROM student_courses;

-- 9. Aggregation: Number of courses per student
SELECT s.name, COUNT(e.course_id) AS total_courses
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.name;

-- 10. Advanced query: Find courses with more than 1 student enrolled
SELECT c.course_name
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
HAVING COUNT(e.student_id) > 1;