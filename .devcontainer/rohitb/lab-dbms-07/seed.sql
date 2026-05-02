USE course_db;

INSERT INTO students (name, email) VALUES
('Rohit', 'rohit@gmail.com'),
('Amit', 'amit@gmail.com'),
('Sneha', 'sneha@gmail.com'),
('Priya', 'priya@gmail.com');

INSERT INTO instructors (name) VALUES
('Dr. Sharma'),
('Prof. Mehta');

INSERT INTO courses (title, instructor_id) VALUES
('DBMS', 1),
('Data Structures', 2),
('Operating Systems', 1);

INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES
(1, 1, '2026-01-01'),
(2, 1, '2026-01-02'),
(3, 2, '2026-01-03'),
(4, 3, '2026-01-04'),
(1, 2, '2026-01-05');