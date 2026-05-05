USE library_db;

-- 1 Join
SELECT m.name, b.title
FROM loans l
JOIN members m ON l.member_id = m.member_id
JOIN books b ON l.book_id = b.book_id;

-- 2 Group By
SELECT member_id, COUNT(*) AS total
FROM loans
GROUP BY member_id;

-- 3 Having
SELECT member_id, COUNT(*) 
FROM loans
GROUP BY member_id
HAVING COUNT(*) > 1;

-- 4 Business question
-- Who has overdue books?
SELECT m.name, b.title
FROM loans l
JOIN members m ON l.member_id = m.member_id
JOIN books b ON l.book_id = b.book_id
WHERE l.return_date IS NULL AND l.due_date < CURDATE();

-- 5 View
CREATE VIEW all_loans AS
SELECT m.name, b.title
FROM loans l
JOIN members m ON l.member_id = m.member_id
JOIN books b ON l.book_id = b.book_id;

SELECT * FROM all_loans;