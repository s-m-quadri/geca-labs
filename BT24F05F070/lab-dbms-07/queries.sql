--------------------------------------------------
-- 1. Show all books with author and category
--------------------------------------------------
SELECT
    b.book_id,
    b.title,
    a.name AS author_name,
    c.category_name,
    b.available_copies
FROM book b
JOIN author a
ON b.author_id = a.author_id
JOIN category c
ON b.category_id = c.category_id;


--------------------------------------------------
-- 2. Borrow history
--------------------------------------------------
SELECT
    m.name AS member_name,
    b.title,
    br.borrow_date,
    br.due_date,
    br.status
FROM borrow br
JOIN member m
ON br.member_id = m.member_id
JOIN book b
ON br.book_id = b.book_id;


--------------------------------------------------
-- 3. Overdue books
--------------------------------------------------
SELECT *
FROM borrow
WHERE due_date < CURRENT_DATE
AND status = 'Borrowed';


--------------------------------------------------
-- 4. Fine details
--------------------------------------------------
SELECT
    m.name,
    f.amount,
    f.paid_status
FROM fine f
JOIN borrow br
ON f.borrow_id = br.borrow_id
JOIN member m
ON br.member_id = m.member_id;


--------------------------------------------------
-- 5. Most borrowed books
--------------------------------------------------
SELECT
    b.title,
    COUNT(*) AS times_borrowed
FROM borrow br
JOIN book b
ON br.book_id = b.book_id
GROUP BY b.title
ORDER BY times_borrowed DESC;