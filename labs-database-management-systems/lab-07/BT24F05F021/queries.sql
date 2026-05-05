-- 1. Multi-table join: List all loans with member and book details
SELECT l.loan_id, m.name, b.title, l.loan_date, l.return_date
FROM Loans l
JOIN Members m ON l.member_id = m.member_id
JOIN Books b ON l.book_id = b.book_id;

-- 2. Aggregate: Count how many books each member borrowed
SELECT m.name, COUNT(l.loan_id) AS total_loans
FROM Members m
JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.name;

-- 3. GROUP BY with HAVING: Members who borrowed more than 1 book
SELECT m.name, COUNT(l.loan_id) AS total_loans
FROM Members m
JOIN Loans l ON m.member_id = l.member_id
GROUP BY m.name
HAVING COUNT(l.loan_id) > 1;

-- 4. Subquery: Find members who have unpaid fines
SELECT name FROM Members
WHERE member_id IN (
    SELECT l.member_id FROM Loans l
    JOIN Fines f ON l.loan_id = f.loan_id
    WHERE f.status = 'Unpaid'
);

-- 5. CREATE VIEW: Active loans (not returned yet)
CREATE VIEW ActiveLoans AS
SELECT l.loan_id, m.name, b.title, l.loan_date
FROM Loans l
JOIN Members m ON l.member_id = m.member_id
JOIN Books b ON l.book_id = b.book_id
WHERE l.return_date IS NULL;

-- 6. Query from view
SELECT * FROM ActiveLoans;

-- 7. Business question: "Which book is most borrowed?"
SELECT b.title, COUNT(l.loan_id) AS borrow_count
FROM Books b
JOIN Loans l ON b.book_id = l.book_id
GROUP BY b.title
ORDER BY borrow_count DESC
LIMIT 1;

-- 8. Stored procedure (stretch): Prevent >3 active loans per member
DELIMITER //
CREATE TRIGGER limit_loans
BEFORE INSERT ON Loans
FOR EACH ROW
BEGIN
    DECLARE active_count INT;
    SELECT COUNT(*) INTO active_count
    FROM Loans
    WHERE member_id = NEW.member_id AND return_date IS NULL;
    IF active_count >= 3 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Loan limit exceeded (max 3 active loans)';
    END IF;
END;
