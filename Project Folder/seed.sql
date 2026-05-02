INSERT INTO student (name, cgpa, branch) VALUES
('Vedant', 8.5, 'IT'),
('Riya', 7.2, 'CS'),
('Amit', 6.8, 'Mechanical'),
('Sneha', 9.1, 'IT');

INSERT INTO company (name, min_cgpa, role) VALUES
('TCS', 6.5, 'Developer'),
('Infosys', 7.0, 'Engineer'),
('Google', 8.5, 'SDE'),
('Wipro', 6.0, 'Analyst');

INSERT INTO application (student_id, company_id, status) VALUES
(1, 1, 'Shortlisted'),
(1, 3, 'Applied'),
(2, 2, 'Rejected'),
(4, 3, 'Shortlisted'),
(3, 4, 'Applied');

INSERT INTO interview (app_id, round_name, result) VALUES
(1, 'Aptitude', 'Pass'),
(1, 'Technical', 'Pass'),
(4, 'Aptitude', 'Pass'),
(4, 'Technical', 'Pass'),
(4, 'HR', 'Pending');