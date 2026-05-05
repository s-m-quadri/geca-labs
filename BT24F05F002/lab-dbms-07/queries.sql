-- queries.sql
-- Example queries for the Student Management System

-- 1. List all students with their major department and enrollment status
SELECT
  s.student_id,
  CONCAT(s.first_name, ' ', s.last_name) AS student_name,
  d.name AS major_department,
  s.status
FROM student s
LEFT JOIN department d ON s.major_dept_id = d.dept_id
ORDER BY s.last_name, s.first_name;

-- 2. Show active courses with instructor name and department
SELECT
  c.course_code,
  c.title,
  CONCAT(i.first_name, ' ', i.last_name) AS instructor,
  d.name AS department,
  c.credits
FROM course c
LEFT JOIN instructor i ON c.instructor_id = i.instructor_id
LEFT JOIN department d ON c.dept_id = d.dept_id
ORDER BY c.course_code;

-- 3. Enrollment count per course for Fall 2024
SELECT
  c.course_code,
  c.title,
  COUNT(e.enrollment_id) AS enrolled_students
FROM course c
LEFT JOIN enrollment e ON e.course_id = c.course_id
LEFT JOIN semester s ON e.semester_id = s.semester_id
WHERE s.term = 'Fall' AND s.year = 2024
GROUP BY c.course_id, c.course_code, c.title
ORDER BY enrolled_students DESC;

-- 4. Student transcript with completed course grades and GPA points
SELECT
  s.student_id,
  CONCAT(s.first_name, ' ', s.last_name) AS student_name,
  c.course_code,
  c.title,
  sem.term,
  sem.year,
  e.grade,
  CASE e.grade
    WHEN 'A' THEN 4.0
    WHEN 'B' THEN 3.0
    WHEN 'C' THEN 2.0
    WHEN 'D' THEN 1.0
    WHEN 'F' THEN 0.0
    ELSE NULL
  END AS grade_points
FROM enrollment e
JOIN student s ON e.student_id = s.student_id
JOIN course c ON e.course_id = c.course_id
JOIN semester sem ON e.semester_id = sem.semester_id
WHERE e.status = 'completed'
ORDER BY s.last_name, s.first_name, sem.year, sem.term;

-- 5. Find students currently enrolled in Fall 2024 and their total registered credits
SELECT
  s.student_id,
  CONCAT(s.first_name, ' ', s.last_name) AS student_name,
  SUM(c.credits) AS total_credits
FROM enrollment e
JOIN student s ON e.student_id = s.student_id
JOIN course c ON e.course_id = c.course_id
JOIN semester sem ON e.semester_id = sem.semester_id
WHERE sem.term = 'Fall' AND sem.year = 2024
  AND e.status = 'enrolled'
GROUP BY s.student_id, s.first_name, s.last_name
ORDER BY total_credits DESC;

-- 6. Courses and current enrollment status (open vs filled based on sample capacity logic)
-- Note: capacity is not modeled explicitly; this query simply reports counts
SELECT
  c.course_code,
  c.title,
  COUNT(e.enrollment_id) AS enrolled_count,
  c.credits
FROM course c
LEFT JOIN enrollment e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_code, c.title, c.credits
ORDER BY enrolled_count DESC;

-- 7. List instructors and the courses they teach
SELECT
  CONCAT(i.first_name, ' ', i.last_name) AS instructor,
  d.name AS department,
  c.course_code,
  c.title
FROM instructor i
LEFT JOIN course c ON i.instructor_id = c.instructor_id
LEFT JOIN department d ON i.dept_id = d.dept_id
ORDER BY i.last_name, c.course_code;

-- 8. Departments with number of students majoring there
SELECT
  d.name AS department,
  COUNT(s.student_id) AS student_count
FROM department d
LEFT JOIN student s ON s.major_dept_id = d.dept_id
GROUP BY d.dept_id, d.name
ORDER BY student_count DESC;

-- 9. Identify students who have earned a grade below C in any completed course
SELECT DISTINCT
  s.student_id,
  CONCAT(s.first_name, ' ', s.last_name) AS student_name,
  e.grade,
  c.course_code,
  c.title
FROM enrollment e
JOIN student s ON e.student_id = s.student_id
JOIN course c ON e.course_id = c.course_id
WHERE e.status = 'completed'
  AND e.grade IN ('D','F')
ORDER BY student_name;

-- 10. Find courses with no enrollments yet
SELECT
  c.course_code,
  c.title,
  COALESCE(COUNT(e.enrollment_id), 0) AS enrollment_count
FROM course c
LEFT JOIN enrollment e ON c.course_id = e.course_id
GROUP BY c.course_id, c.course_code, c.title
HAVING enrollment_count = 0;
