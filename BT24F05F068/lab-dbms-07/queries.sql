USE library_db;

-- Aggregate + GROUP BY
SELECT 
    c.cat_name AS category,
    COUNT(b.book_id) AS book_count,
    ROUND(AVG(CHAR_LENGTH(b.book_title)), 2) AS avg_title_length
FROM categories c
LEFT JOIN books b ON c.cat_id = b.cat_id
GROUP BY c.cat_id, c.cat_name
HAVING COUNT(b.book_id) > 0
ORDER BY book_count DESC;

-- 1. View Query
SELECT * FROM v_book_directory WHERE cat_name = 'Technology';

-- 2. Subquery
SELECT book_title FROM books
WHERE cat_id IN (SELECT cat_id FROM categories WHERE cat_name LIKE 'T%');

-- 3. Join + Aggregate
SELECT c.cat_name, COUNT(b.book_id) AS total_books
FROM categories c
LEFT JOIN books b ON c.cat_id = b.cat_id
GROUP BY c.cat_name;

-- 4. HAVING
SELECT c.cat_name, COUNT(b.book_id) AS book_count
FROM categories c
JOIN books b ON c.cat_id = b.cat_id
GROUP BY c.cat_name
HAVING COUNT(b.book_id) > 1;

-- 5. Oldest Book (based on ID)
SELECT book_title
FROM books
ORDER BY book_id ASC
LIMIT 1;

-- 6. Pattern Matching
SELECT book_title
FROM books
WHERE book_title LIKE 'The%';

-- 7. Join with Ordering
SELECT b.book_title, c.cat_name
FROM books b
JOIN categories c ON b.cat_id = c.cat_id
ORDER BY c.cat_name ASC;

-- 8. NULL Check
SELECT c.cat_name
FROM categories c
LEFT JOIN books b ON c.cat_id = b.cat_id
WHERE b.book_id IS NULL;