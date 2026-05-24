-- seed.sql: Sample Data for Student Attendance System
-- -----------------------------------------------

-- Insert Courses
INSERT INTO Courses (course_name) VALUES
('Computer Science'),
('Mechanical Engineering'),
('Electrical Engineering'),
('Civil Engineering'),
('Mathematics');

-- Insert Teachers
INSERT INTO Teachers (name, email) VALUES
('Dr. A. Sharma', 'asharma@univ.edu'),
('Prof. B. Singh', 'bsingh@univ.edu'),
('Ms. C. Patel', 'cpatel@univ.edu'),
('Mr. D. Kumar', 'dkumar@univ.edu'),
('Mrs. E. Rao', 'erao@univ.edu');

-- Insert Classes
INSERT INTO Classes (class_name, teacher_id) VALUES
('Data Structures', 1),
('Thermodynamics', 2),
('Circuits', 3),
('Structural Analysis', 4),
('Linear Algebra', 5);

-- Insert Students
INSERT INTO Students (name, email, course_id) VALUES
('Ankit Verma', 'ankit.verma@univ.edu', 1),
('Priya Singh', 'priya.singh@univ.edu', 1),
('Rahul Mehra', 'rahul.mehra@univ.edu', 2),
('Sneha Gupta', 'sneha.gupta@univ.edu', 2),
('Vikas Jain', 'vikas.jain@univ.edu', 3),
('Meera Nair', 'meera.nair@univ.edu', 3),
('Amit Joshi', 'amit.joshi@univ.edu', 4),
('Ritu Sharma', 'ritu.sharma@univ.edu', 4),
('Karan Patel', 'karan.patel@univ.edu', 5),
('Simran Kaur', 'simran.kaur@univ.edu', 5);

-- Insert Attendance (sample for 3 days)
INSERT INTO Attendance (student_id, class_id, date, status) VALUES
-- Day 1
(1, 1, '2026-05-01', 'Present'),
(2, 1, '2026-05-01', 'Absent'),
(3, 2, '2026-05-01', 'Present'),
(4, 2, '2026-05-01', 'Present'),
(5, 3, '2026-05-01', 'Absent'),
(6, 3, '2026-05-01', 'Present'),
(7, 4, '2026-05-01', 'Present'),
(8, 4, '2026-05-01', 'Absent'),
(9, 5, '2026-05-01', 'Present'),
(10, 5, '2026-05-01', 'Present'),
-- Day 2
(1, 1, '2026-05-02', 'Absent'),
(2, 1, '2026-05-02', 'Present'),
(3, 2, '2026-05-02', 'Present'),
(4, 2, '2026-05-02', 'Absent'),
(5, 3, '2026-05-02', 'Present'),
(6, 3, '2026-05-02', 'Present'),
(7, 4, '2026-05-02', 'Absent'),
(8, 4, '2026-05-02', 'Present'),
(9, 5, '2026-05-02', 'Present'),
(10, 5, '2026-05-02', 'Absent'),
-- Day 3
(1, 1, '2026-05-03', 'Present'),
(2, 1, '2026-05-03', 'Present'),
(3, 2, '2026-05-03', 'Absent'),
(4, 2, '2026-05-03', 'Present'),
(5, 3, '2026-05-03', 'Present'),
(6, 3, '2026-05-03', 'Absent'),
(7, 4, '2026-05-03', 'Present'),
(8, 4, '2026-05-03', 'Present'),
(9, 5, '2026-05-03', 'Absent'),
(10, 5, '2026-05-03', 'Present');
