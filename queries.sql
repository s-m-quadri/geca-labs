SELECT * FROM Students;

SELECT * FROM Books;

SELECT Students.student_name, Books.book_name
FROM IssueBooks
JOIN Students ON IssueBooks.student_id = Students.student_id
JOIN Books ON IssueBooks.book_id = Books.book_id;

SELECT course, COUNT(*) AS total_students
FROM Students
GROUP BY course;