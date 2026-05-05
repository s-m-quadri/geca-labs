INSERT INTO Members (name, email, phone) VALUES
('Amit Sharma', 'amit@example.com', '9876543210'),
('Priya Desai', 'priya@example.com', '9123456789'),
('Ravi Kumar', 'ravi@example.com', '9988776655'),
('Sneha Patil', 'sneha@example.com', '9112233445');

INSERT INTO Books (title, author, genre, published_year) VALUES
('DBMS Fundamentals', 'Elmasri', 'Education', 2015),
('Operating Systems', 'Silberschatz', 'Education', 2018),
('The Alchemist', 'Paulo Coelho', 'Fiction', 1993),
('Wings of Fire', 'A.P.J. Abdul Kalam', 'Biography', 1999),
('Clean Code', 'Robert Martin', 'Programming', 2008);

INSERT INTO Loans (member_id, book_id, loan_date, return_date) VALUES
(1, 1, '2026-04-01', '2026-04-10'),
(2, 3, '2026-04-02', NULL),
(3, 2, '2026-04-05', '2026-04-12'),
(4, 5, '2026-04-07', NULL);

INSERT INTO Fines (loan_id, amount, status) VALUES
(1, 50.00, 'Paid'),
(2, 100.00, 'Unpaid');
