# Library Management System - Schema

Entities:
- Members
- Books
- Staff
- Borrow

Relationships:
- One member can borrow many books (1:N)
- One book can be borrowed many times (1:N)
- Borrow table connects Members, Books, Staff

Keys:
- Primary Keys: member_id, book_id, staff_id, borrow_id
- Foreign Keys:
  - member_id → members
  - book_id → books
  - staff_id → staff