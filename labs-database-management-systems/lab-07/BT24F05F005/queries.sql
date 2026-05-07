USE library_db;

-- Q1: Show all books with their authors
SELECT
	books.book_id,
	books.title,
	books.genre,
	books.published_year,
	authors.name AS author_name
FROM books
JOIN authors ON books.author_id = authors.author_id
ORDER BY books.title;

-- Q2: Show all borrowed books with member names
SELECT
	members.full_name,
	books.title,
	loans.loan_date,
	loans.return_date
FROM loans
JOIN members ON loans.member_id = members.member_id
JOIN books ON loans.book_id = books.book_id
ORDER BY loans.loan_date DESC;

-- Q3: Count the number of books borrowed by each member
SELECT
	members.member_id,
	members.full_name,
	COUNT(loans.loan_id) AS borrowed_books
FROM members
LEFT JOIN loans ON members.member_id = loans.member_id
GROUP BY members.member_id, members.full_name
ORDER BY borrowed_books DESC, members.full_name;

-- Q4: Show currently borrowed books that have not been returned yet
SELECT
	members.full_name,
	books.title,
	loans.loan_date
FROM loans
JOIN members ON loans.member_id = members.member_id
JOIN books ON loans.book_id = books.book_id
WHERE loans.return_date IS NULL
ORDER BY loans.loan_date;

-- Q5: Show authors with the number of books they have written
SELECT
	authors.author_id,
	authors.name,
	COUNT(books.book_id) AS total_books
FROM authors
LEFT JOIN books ON authors.author_id = books.author_id
GROUP BY authors.author_id, authors.name
ORDER BY total_books DESC, authors.name;

-- Q6: Show members who have never borrowed a book
SELECT
	members.member_id,
	members.full_name,
	members.email
FROM members
LEFT JOIN loans ON members.member_id = loans.member_id
GROUP BY members.member_id, members.full_name, members.email
HAVING COUNT(loans.loan_id) = 0
ORDER BY members.full_name;