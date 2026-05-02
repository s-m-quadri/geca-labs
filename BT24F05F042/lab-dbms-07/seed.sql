-- Insert students
INSERT INTO students VALUES
(1, 'Asha', 'CS'),
(2, 'Ravi', 'IT'),
(3, 'Neha', 'CS'),
(4, 'Karan', 'ECE'),
(5, 'Pooja', 'CS'),
(6, 'Arjun', 'IT');

-- Insert faculty
INSERT INTO faculty VALUES
(101, 'Dr. Mehta', 'CS'),
(102, 'Dr. Shah', 'IT'),
(103, 'Dr. Rao', 'ECE');

-- Insert courses (with credits)
INSERT INTO courses VALUES
(201, 'DBMS', 4, 101),
(202, 'Operating Systems', 3, 101),
(203, 'Networks', 3, 102),
(204, 'Electronics', 3, 103);

-- Insert enrollments (with semester)
INSERT INTO enrollments VALUES
(1, 201, 'A', 'Sem1'),
(1, 202, 'B', 'Sem1'),
(2, 201, 'B', 'Sem1'),
(2, 203, 'A', 'Sem2'),
(3, 201, 'A', 'Sem1'),
(3, 204, 'B', 'Sem2'),
(4, 204, 'C', 'Sem1'),
(5, 201, 'A', 'Sem1'),
(5, 202, 'A', 'Sem2'),
(6, 203, 'B', 'Sem2');