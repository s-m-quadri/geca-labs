-- Create the database
DROP DATABASE IF EXISTS library_db;
CREATE DATABASE library_db;
USE library_db;

-- Parent table: Book Categories
CREATE TABLE categories (
    cat_id INT AUTO_INCREMENT PRIMARY KEY,
    cat_name VARCHAR(80) NOT NULL
);

-- Child table: Books linked to a category
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    book_title VARCHAR(100) NOT NULL,
    cat_id INT NOT NULL,
    FOREIGN KEY (cat_id) REFERENCES categories(cat_id)
);

-- View: Book directory with category
CREATE OR REPLACE VIEW v_book_directory AS
SELECT b.book_title, c.cat_name
FROM books b
JOIN categories c ON b.cat_id = c.cat_id;