-- 1. Join Query
SELECT m.name, b.title, br.borrow_date
FROM borrow br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id;

-- 2. Aggregate Query
SELECT m.name, COUNT(br.book_id) AS total_books
FROM members m
JOIN borrow br ON m.member_id = br.member_id
GROUP BY m.name;

-- 3. HAVING Clause
SELECT m.name, COUNT(*) AS total
FROM borrow br
JOIN members m ON br.member_id = m.member_id
GROUP BY m.name
HAVING COUNT(*) > 1;

-- 4. Subquery
SELECT title
FROM books
WHERE book_id IN (
    SELECT book_id FROM borrow WHERE return_date IS NULL
);

-- 5. Business Question
SELECT name
FROM members
WHERE member_id = (
    SELECT member_id
    FROM borrow
    GROUP BY member_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- 6. View
CREATE VIEW active_borrows AS
SELECT m.name, b.title
FROM borrow br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id
WHERE return_date IS NULL;

SELECT * FROM active_borrows;

-- 7. Available Books
SELECT title FROM books
WHERE book_id NOT IN (
    SELECT book_id FROM borrow WHERE return_date IS NULL
);

-- 8. Staff Activity
SELECT s.name, COUNT(br.borrow_id) AS handled
FROM staff s
JOIN borrow br ON s.staff_id = br.staff_id
GROUP BY s.name;