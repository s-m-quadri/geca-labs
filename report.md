# Enterprise Hotel Management Database

### Overview
This project serves as a structured database solution for a Hotel Management System. It efficiently organizes operational data including staff management, room categorization, customer bookings, and financial invoicing.

### Database Architecture
*   **tbl_departments** & **tbl_employees**: Human resources tracking.
*   **tbl_guests**: Customer relationship data.
*   **tbl_room_categories** & **tbl_rooms**: Inventory management.
*   **tbl_bookings** & **tbl_invoices**: Transactional records.

### Implementation Steps
1. Execute the schema script (`ddl.sql`).
2. Populate the tables with dummy data (`seed.sql`).
3. Run reporting metrics (`queries.sql`).

### Summary
By utilizing primary and foreign keys, this MySQL architecture ensures referential integrity across all hotel operations, preventing orphaned records and ensuring accurate financial reporting.