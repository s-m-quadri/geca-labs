# Database Schema: Library Management System

## Entities and Attributes

1. **Categories**
   - `cat_id` (PK)
   - `cat_name`

2. **Books**
   - `book_id` (PK)
   - `book_title`
   - `cat_id` (FK)

3. **Members**
   - `member_id` (PK)
   - `member_name`
   - `email`

4. **Borrowings**
   - `borrow_id` (PK)
   - `book_id` (FK)
   - `member_id` (FK)
   - `borrow_date`

## Relationships
- Categories → Books (1:N)
- Books → Borrowings (1:N)
- Members → Borrowings (1:N)