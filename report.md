Problem  
A small library wants to track members, books, loans, and fines. Users are librarians who need quick queries for overdue books, unpaid fines, and borrowing trends.

Design
Normalized into 4 tables: Members, Books, Loans, Fines.
Avoided redundancy (e.g., fines linked only to loans, not directly to members).
Foreign key chain ensures referential integrity.

Sample Results
Query 1 shows all loans with member and book details.
Query 4 identifies members with unpaid fines.
Query 7 answers: “The most borrowed book is DBMS Fundamentals.”

Limits
No support for reservations or multiple copies of the same book.
Could add staff accounts, book categories, and overdue notifications with more time.

References
MySQL documentation for triggers and views.
Class notes from DBMS lab sequence.