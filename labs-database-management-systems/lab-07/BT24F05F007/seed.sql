-- Members
INSERT INTO members (name, email) VALUES
('Rahul', 'rahul@gmail.com'),
('Sneha', 'sneha@gmail.com'),
('Amit', 'amit@gmail.com');

-- Books
INSERT INTO books (title, author) VALUES
('DBMS Basics', 'Korth'),
('Operating Systems', 'Galvin'),
('Computer Networks', 'Tanenbaum'),
('Data Structures', 'Sahni');

-- Staff
INSERT INTO staff (name) VALUES
('Admin1'),
('Admin2');

-- Borrow Records
INSERT INTO borrow (member_id, book_id, staff_id, borrow_date, return_date) VALUES
(1, 1, 1, '2026-01-01', '2026-01-10'),
(2, 2, 2, '2026-01-05', NULL),
(3, 3, 1, '2026-01-07', NULL),
(1, 4, 2, '2026-01-10', '2026-01-15');