-- Instructors
INSERT INTO instructor (name, email) VALUES
('Dr. Sharma', 'sharma@gmail.com'),
('Prof. Mehta', 'mehta@gmail.com');

-- Students
INSERT INTO student (name, email) VALUES
('Amit', 'amit@gmail.com'),
('Neha', 'neha@gmail.com'),
('Rahul', 'rahul@gmail.com');

-- Courses
INSERT INTO course (title, instructor_id) VALUES
('DBMS Basics', 1),
('Web Development', 2);


INSERT INTO enrollment (student_id, course_id, status) VALUES
(1, 1, 'active');