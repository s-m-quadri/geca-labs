USE course_db;

-- 1. List all students with their enrolled courses
SELECT s.name AS student, c.title AS course
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 2. Count students per course
SELECT c.title, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.title;

-- 3. Students enrolled in DBMS
SELECT name
FROM students
WHERE student_id IN (
    SELECT student_id
    FROM enrollments
    WHERE course_id = 1
);

-- 4. Full join across all tables
SELECT s.name AS student, c.title AS course, i.name AS instructor
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
JOIN instructors i ON c.instructor_id = i.instructor_id;

-- 5. Create a view
CREATE VIEW student_course_view AS
SELECT s.name AS student, c.title AS course
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 6. Use the view
SELECT * FROM student_course_view;