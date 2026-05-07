SELECT s.name, c.title
FROM student s
JOIN enrollment e ON s.student_id = e.student_id
JOIN course c ON e.course_id = c.course_id;

SELECT c.title, COUNT(e.student_id) AS total_students
FROM course c
LEFT JOIN enrollment e ON c.course_id = e.course_id
GROUP BY c.course_id, c.title;

SELECT s.name, COUNT(e.course_id) AS course_count
FROM student s
JOIN enrollment e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name
HAVING COUNT(e.course_id) > 1;