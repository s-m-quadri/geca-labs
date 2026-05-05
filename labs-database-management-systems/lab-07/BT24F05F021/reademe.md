Overview
This project is the capstone for the DBMS lab sequence. It implements a small Library Management System in MySQL, designed to track members, books, loans, and fines. The schema, seed data, queries, and report demonstrate database design principles, normalization, and practical SQL usage.

📂 Project Structure
ddl.sql – Database schema (tables, primary keys, foreign keys).
schema.md – ER description and ASCII diagram of entities and relationships.
seed.sql – Sample data to populate tables.
queries.sql – Non-trivial SQL queries (joins, aggregates, subqueries, views, business questions, trigger).
report.md – Written explanation of problem, design, sample results, limitations, and references.
README.md – Project overview and usage instructions.

🗄️ Schema
Members – Library members with contact details.
Books – Collection of books with metadata.
Loans – Records of which member borrowed which book, with loan/return dates.
Fines – Penalties linked to loans for overdue returns.

Relationships:
Members → Loans → Fines (chain of foreign keys).
Books → Loans (1:N relationship).

🚀 Setup & Usage
Clone your fork of the repository.
Open the Codespace (branch lab-dbms-07).

Run schema:
bash
mysql < ddl.sql
Seed data:

bash
mysql < seed.sql

Execute queries:
bash
mysql < queries.sql

✅ Features
≥4 tables with clear primary keys and foreign keys.
Chain of foreign keys ensuring referential integrity.
Seed data with enough rows for meaningful queries.
≥8 queries covering joins, aggregates, subqueries, views, and business questions.
Trigger enforcing rule: max 3 active loans per member.
Report documenting design choices, sample outputs, and limitations.

📊 Example Queries
List all loans with member and book details.
Count how many books each member borrowed.
Identify members with unpaid fines.
Find the most borrowed book.
View active loans (not yet returned).

🔮 Future Scope
Add Reservations table for book requests.
Support multiple authors per book via junction table.
Track multiple copies per book.
Role-based access for librarians vs members.
Automated fine calculation and overdue notifications.

📖 References
MySQL Documentation (Triggers, Views, Constraints).
DBMS Lab Notes and Coursework.