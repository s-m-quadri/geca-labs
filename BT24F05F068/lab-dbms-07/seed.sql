USE library_db;

-- Insert Categories
INSERT INTO categories (cat_name) VALUES
  ('Fiction'),
  ('Science'),
  ('History'),
  ('Technology');

-- Insert Books
INSERT INTO books (book_title, cat_id) VALUES
  ('The Alchemist', 1),
  ('A Brief History of Time', 2),
  ('Sapiens', 3),
  ('Clean Code', 4),
  ('The Pragmatic Programmer', 4);