--------------------------------------------------
-- AUTHORS
--------------------------------------------------
INSERT INTO author(name, nationality) VALUES
('J.K. Rowling', 'British'),
('George Orwell', 'British'),
('Chetan Bhagat', 'Indian'),
('Dan Brown', 'American');

--------------------------------------------------
-- CATEGORIES
--------------------------------------------------
INSERT INTO category(category_name, description) VALUES
('Fantasy', 'Fantasy novels'),
('Fiction', 'Fiction books'),
('Technology', 'Technical books'),
('Biography', 'Life stories');

--------------------------------------------------
-- MEMBERS
--------------------------------------------------
INSERT INTO member(name, email, phone, membership_type) VALUES
('Rohan Pawar', 'rohan@gmail.com', '9876543210', 'Premium'),
('Amit Sharma', 'amit@gmail.com', '9876543211', 'Standard'),
('Sneha Patil', 'sneha@gmail.com', '9876543212', 'Student');

--------------------------------------------------
-- BOOKS
--------------------------------------------------
INSERT INTO book(
    title,
    author_id,
    category_id,
    isbn,
    total_copies,
    available_copies
)
VALUES
('Harry Potter', 1, 1, 'ISBN001', 10, 10),
('1984', 2, 2, 'ISBN002', 8, 8),
('2 States', 3, 2, 'ISBN003', 6, 6),
('The Da Vinci Code', 4, 2, 'ISBN004', 5, 5);

--------------------------------------------------
-- BORROW RECORDS
--------------------------------------------------
INSERT INTO borrow(
    member_id,
    book_id,
    due_date,
    status
)
VALUES
(1, 1, CURRENT_DATE + 7, 'Borrowed'),

(2, 2, CURRENT_DATE + 7, 'Borrowed');

--------------------------------------------------
-- FINES
--------------------------------------------------
INSERT INTO fine(
    borrow_id,
    amount,
    paid_status
)
VALUES
(1, 50.00, 'Unpaid');