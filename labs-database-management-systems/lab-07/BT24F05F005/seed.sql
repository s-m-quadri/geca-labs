USE library_db;

INSERT INTO authors (name, country) VALUES
('J.K. Rowling', 'UK'),
('George Orwell', 'UK'),
('Paulo Coelho', 'Brazil'),
('Dan Brown', 'USA');

INSERT INTO books (title, genre, published_year, author_id) VALUES
('Harry Potter', 'Fantasy', 1997, 1),
('1984', 'Dystopian', 1949, 2),
('Animal Farm', 'Political Satire', 1945, 2),
('The Alchemist', 'Fiction', 1988, 3),
('Da Vinci Code', 'Thriller', 2003, 4),
('Inferno', 'Thriller', 2013, 4),
('Brida', 'Fantasy', 1990, 3),
('Fantastic Beasts', 'Fantasy', 2001, 1);

INSERT INTO members (full_name, email, join_date) VALUES
('Alice Johnson', 'alice@gmail.com', '2024-01-10'),
('Bob Smith', 'bob@gmail.com', '2024-02-12'),
('Charlie Brown', 'charlie@gmail.com', '2024-03-01'),
('David Lee', 'david@gmail.com', '2024-03-20'),
('Emma Watson', 'emma@gmail.com', '2024-04-01'),
('Frank Miller', 'frank@gmail.com', '2024-04-05'),
('Grace Hall', 'grace@gmail.com', '2024-04-12'),
('Henry Clark', 'henry@gmail.com', '2024-04-18');

INSERT INTO loans (member_id, book_id, loan_date, return_date) VALUES
(1, 1, '2025-01-01', '2025-01-10'),
(2, 2, '2025-01-03', '2025-01-12'),
(3, 3, '2025-01-05', NULL),
(4, 4, '2025-01-08', '2025-01-15'),
(5, 5, '2025-01-10', NULL),
(6, 6, '2025-01-11', '2025-01-20'),
(7, 7, '2025-01-13', NULL),
(8, 8, '2025-01-15', '2025-01-22'),
(1, 2, '2025-02-01', NULL),
(2, 5, '2025-02-05', NULL);