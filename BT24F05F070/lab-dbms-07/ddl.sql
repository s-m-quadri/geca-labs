DROP DATABASE IF EXISTS library_management;
CREATE DATABASE library_management;

\c library_management;

--------------------------------------------------
-- MEMBER TABLE
--------------------------------------------------
CREATE TABLE member (
    member_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    
    email VARCHAR(100) UNIQUE NOT NULL,
    
    phone VARCHAR(15) UNIQUE,
    
    join_date DATE NOT NULL DEFAULT CURRENT_DATE,
    
    membership_type VARCHAR(20) NOT NULL
        CHECK (membership_type IN ('Standard', 'Premium', 'Student'))
);

--------------------------------------------------
-- AUTHOR TABLE
--------------------------------------------------
CREATE TABLE author (
    author_id SERIAL PRIMARY KEY,
    
    name VARCHAR(100) NOT NULL,
    
    nationality VARCHAR(50)
);

--------------------------------------------------
-- CATEGORY TABLE
--------------------------------------------------
CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    
    category_name VARCHAR(100) UNIQUE NOT NULL,
    
    description TEXT
);

--------------------------------------------------
-- BOOK TABLE
--------------------------------------------------
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    
    title VARCHAR(150) NOT NULL,
    
    author_id INT NOT NULL,
    
    category_id INT NOT NULL,
    
    isbn VARCHAR(20) UNIQUE NOT NULL,
    
    total_copies INT NOT NULL
        CHECK (total_copies >= 0),
    
    available_copies INT NOT NULL
        CHECK (
            available_copies >= 0
            AND
            available_copies <= total_copies
        ),

    FOREIGN KEY (author_id)
        REFERENCES author(author_id),

    FOREIGN KEY (category_id)
        REFERENCES category(category_id)
);

--------------------------------------------------
-- BORROW TABLE
--------------------------------------------------
CREATE TABLE borrow (
    borrow_id SERIAL PRIMARY KEY,
    
    member_id INT NOT NULL,
    
    book_id INT NOT NULL,
    
    borrow_date DATE NOT NULL DEFAULT CURRENT_DATE,
    
    due_date DATE NOT NULL,
    
    return_date DATE,
    
    status VARCHAR(20) NOT NULL
        CHECK (status IN ('Borrowed', 'Returned', 'Overdue')),

    CHECK (due_date >= borrow_date),

    FOREIGN KEY (member_id)
        REFERENCES member(member_id),

    FOREIGN KEY (book_id)
        REFERENCES book(book_id)
);

--------------------------------------------------
-- FINE TABLE
--------------------------------------------------
CREATE TABLE fine (
    fine_id SERIAL PRIMARY KEY,
    
    borrow_id INT UNIQUE NOT NULL,
    
    amount DECIMAL(10,2) NOT NULL
        CHECK (amount >= 0),
    
    paid_status VARCHAR(20) NOT NULL
        CHECK (paid_status IN ('Paid', 'Unpaid')),
    
    paid_date DATE,

    FOREIGN KEY (borrow_id)
        REFERENCES borrow(borrow_id)
);

--------------------------------------------------
-- INDEXES
--------------------------------------------------
CREATE INDEX idx_book_title ON book(title);

CREATE INDEX idx_member_name ON member(name);

CREATE INDEX idx_borrow_status ON borrow(status);

--------------------------------------------------
-- TRIGGER FUNCTION
-- Reduce available copies when book borrowed
--------------------------------------------------
CREATE OR REPLACE FUNCTION reduce_book_copies()
RETURNS TRIGGER AS $$
BEGIN

    UPDATE book
    SET available_copies = available_copies - 1
    WHERE book_id = NEW.book_id;

    RETURN NEW;

END;
$$ LANGUAGE plpgsql;

--------------------------------------------------
-- TRIGGER
--------------------------------------------------
CREATE TRIGGER trg_reduce_book_copies
AFTER INSERT ON borrow
FOR EACH ROW
EXECUTE FUNCTION reduce_book_copies();