-- seed.sql
-- Populate the Student Management System with sample data

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE enrollment;
TRUNCATE TABLE course;
TRUNCATE TABLE semester;
TRUNCATE TABLE student;
TRUNCATE TABLE instructor;
TRUNCATE TABLE department;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO department (dept_code, name, building) VALUES
('CS', 'Computer Science', 'Science Hall'),
('ENG', 'English', 'Liberal Arts'),
('MATH', 'Mathematics', 'Math Center'),
('BUS', 'Business', 'Commerce Building');

INSERT INTO instructor (first_name, last_name, email, phone, dept_id, hire_date) VALUES
('Aisha', 'Khan', 'aisha.khan@university.edu', '555-0101', 1, '2018-08-15'),
('Rohit', 'Patel', 'rohit.patel@university.edu', '555-0102', 2, '2019-01-10'),
('Maria', 'Garcia', 'maria.garcia@university.edu', '555-0103', 3, '2020-07-22'),
('Samuel', 'Lee', 'samuel.lee@university.edu', '555-0104', 4, '2017-03-05');

INSERT INTO student (first_name, last_name, email, birth_date, enrollment_date, major_dept_id, status) VALUES
('Neha', 'Joshi', 'neha.joshi@student.edu', '2003-05-10', '2022-08-20', 1, 'active'),
('Aditya', 'Sharma', 'aditya.sharma@student.edu', '2002-11-08', '2021-08-20', 1, 'active'),
('Priya', 'Verma', 'priya.verma@student.edu', '2004-02-18', '2023-01-15', 2, 'active'),
('Emily', 'Brown', 'emily.brown@student.edu', '2001-12-02', '2020-08-20', 3, 'graduated'),
('Joshua', 'Smith', 'joshua.smith@student.edu', '2003-09-14', '2022-08-20', 4, 'active');

INSERT INTO semester (term, year, start_date, end_date) VALUES
('Spring', 2024, '2024-01-15', '2024-05-01'),
('Fall', 2024, '2024-08-20', '2024-12-10');

INSERT INTO course (course_code, title, description, credits, dept_id, instructor_id) VALUES
('CS101', 'Introduction to Programming', 'Fundamentals of programming using Python.', 4, 1, 1),
('CS204', 'Data Structures', 'Study of arrays, lists, trees, and graphs.', 4, 1, 1),
('ENG105', 'Academic Writing', 'Writing essays, research papers, and proposals.', 3, 2, 2),
('MATH201', 'Calculus II', 'Advanced calculus topics including integration techniques.', 4, 3, 3),
('BUS301', 'Principles of Management', 'Management theory, organizational behavior, and strategy.', 3, 4, 4);

INSERT INTO enrollment (student_id, course_id, semester_id, enrollment_date, grade, status) VALUES
(1, 1, 1, '2024-01-16', 'A', 'completed'),
(1, 2, 1, '2024-01-16', 'B', 'completed'),
(2, 1, 1, '2024-01-17', 'A', 'completed'),
(2, 4, 1, '2024-01-17', 'C', 'completed'),
(3, 3, 1, '2024-01-18', 'B', 'completed'),
(4, 4, 1, '2024-01-18', 'A', 'completed'),
(4, 3, 1, '2024-01-18', 'A', 'completed'),
(5, 5, 2, '2024-08-21', NULL, 'enrolled'),
(1, 5, 2, '2024-08-21', NULL, 'enrolled'),
(3, 1, 2, '2024-08-22', NULL, 'enrolled');
