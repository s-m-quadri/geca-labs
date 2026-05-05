USE library_db;

INSERT INTO authors (name) VALUES
('Rowling'), ('Orwell');

INSERT INTO books (title, author_id) VALUES
('Harry Potter',1), ('1984',2), ('Animal Farm',2);

INSERT INTO members (name) VALUES
('Alice'), ('Bob'), ('Charlie'), ('Diana');

INSERT INTO loans (book_id, member_id, due_date, return_date) VALUES
(1,1,'2024-01-10',NULL),
(2,2,'2024-01-12','2024-01-11'),
(3,3,'2024-01-15',NULL),
(1,4,'2024-01-18',NULL);