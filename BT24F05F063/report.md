-- ============================================================================
-- Hotel Management System - Project Report
-- Database: view_lab
-- Created: May 2, 2026
-- ============================================================================

/*

PROJECT OVERVIEW
================================================================================
This Hotel Management System database demonstrates a complete DBMS mini project
using MySQL with normalized schema design, proper constraints, relationships,
and practical business queries.

DATABASE NAME: view_lab
SQL VARIANT: MySQL (NOT PostgreSQL)


SCHEMA DESIGN & NORMALIZATION
================================================================================

1. GUESTS TABLE
   Purpose: Store guest information
   Primary Key: guest_id (AUTO_INCREMENT)
   Columns:
     - guest_id: Unique identifier for each guest
     - name: Guest's full name (VARCHAR 100)
     - phone: Contact phone number (VARCHAR 15)
     - email: Email address (VARCHAR 100)
     - created_at: Timestamp of record creation

   Design Rationale:
   - Separate guests table follows 1NF by storing atomic values
   - Phone and email are NOT combined into one field
   - Each guest has a unique ID for referential integrity

2. ROOMS TABLE
   Purpose: Store room inventory and status
   Primary Key: room_id (AUTO_INCREMENT)
   Columns:
     - room_id: Unique room identifier
     - room_type: Type of room (single, double, suite)
     - price: Nightly rate (DECIMAL 10,2 for currency precision)
     - status: Current availability status (available, occupied, maintenance)
     - created_at: Timestamp of record creation

   Design Rationale:
   - Status field allows dynamic room management
   - Separate room types with consistent pricing
   - DECIMAL used for accurate currency representation
   - DEFAULT 'available' ensures new rooms are bookable

3. STAFF TABLE
   Purpose: Store staff/employee information
   Primary Key: staff_id (AUTO_INCREMENT)
   Columns:
     - staff_id: Unique employee identifier
     - name: Employee's full name (VARCHAR 100)
     - role: Job position/title (VARCHAR 50)
     - salary: Annual salary (DECIMAL 10,2)
     - created_at: Timestamp of record creation

   Design Rationale:
   - Independent staff table for HR management
   - Role field allows department/position tracking
   - Separate table enables future payroll integration

4. BOOKINGS TABLE
   Purpose: Store booking transactions and reservations
   Primary Key: booking_id (AUTO_INCREMENT)
   Foreign Keys:
     - guest_id (references guests.guest_id)
     - room_id (references rooms.room_id)
   Columns:
     - booking_id: Unique booking identifier
     - guest_id: Reference to guests table (NOT NULL)
     - room_id: Reference to rooms table (NOT NULL)
     - check_in: Check-in date (DATE)
     - check_out: Check-out date (DATE)
     - total_amount: Total booking amount (DECIMAL 10,2)
     - created_at: Timestamp of record creation

   Design Rationale:
   - Follows 3NF: depends only on primary key
   - FOREIGN KEY constraints ensure referential integrity
   - ON DELETE CASCADE ensures orphaned records are cleaned up
   - Separate check_in/check_out dates follow 1NF
   - Relationship creates logical database model


KEY CONSTRAINTS & FEATURES
================================================================================

1. PRIMARY KEY CONSTRAINTS
   - All tables have AUTO_INCREMENT integer primary keys
   - Ensures uniqueness and fast lookup

2. FOREIGN KEY CONSTRAINTS
   - bookings.guest_id → guests.guest_id
   - bookings.room_id → rooms.room_id
   - Maintains referential integrity
   - ON DELETE CASCADE prevents orphaned records

3. NOT NULL CONSTRAINTS
   - Applied to essential data fields
   - Guests: name, phone, email
   - Rooms: room_type, price, status
   - Staff: name, role, salary
   - Bookings: guest_id, room_id, check_in, check_out, total_amount

4. DEFAULT VALUES
   - rooms.status DEFAULT 'available'
   - created_at timestamps DEFAULT CURRENT_TIMESTAMP

5. DATA TYPES
   - INT: Primary/foreign keys, counts
   - VARCHAR: Names, types, roles, status
   - DECIMAL(10,2): Prices, salaries, amounts (currency precision)
   - DATE: Dates without time
   - TIMESTAMP: Audit trail

6. INDEXES
   - Native indexes on foreign keys for JOIN performance
   - Index on rooms.status for frequent filtering
   - Index on bookings dates for date range queries


NORMALIZATION LEVELS
================================================================================

FIRST NORMAL FORM (1NF):
✓ All values are atomic (no repeating groups)
✓ All records have a unique identifier
✓ Each column contains consistent data types

SECOND NORMAL FORM (2NF):
✓ Meets 1NF requirements
✓ All non-key attributes depend on the entire primary key
✓ No partial dependencies

THIRD NORMAL FORM (3NF):
✓ Meets 2NF requirements
✓ All non-key attributes depend only on primary key
✓ No transitive dependencies
✓ Example: booking.total_amount depends on booking_id, not derived from other fields


BUSINESS RULES
================================================================================

1. A Guest can have multiple bookings
2. A Room can be booked multiple times in different periods
3. Each Booking links exactly one Guest to exactly one Room
4. Room status must be one of: available, occupied, maintenance
5. Check-out date must be after check-in date
6. Total amount should reflect the room price × number of nights


SAMPLE DATA INCLUDED
================================================================================
- 5 Guests with contact information
- 6 Rooms with varying types and prices
- 5 Staff members with different roles
- 5 Bookings showing guest-room relationships

This data is realistic and demonstrates:
- Guest relationships with multiple bookings
- Room occupancy status variations
- Diverse staff roles and compensation
- Complex booking scenarios


KEY QUERIES PROVIDED
================================================================================
1. Guest Booking Details (JOIN query)
2. Total Revenue Analysis (AGGREGATION)
3. Bookings Per Guest (GROUP BY)
4. Highest Priced Room Bookings (SUBQUERY)
5. Available Rooms Listing (FILTERING)
6. Ongoing Bookings (DATE FILTERING)
7. Room Type Revenue (GROUP BY aggregation)
8. Guest Booking History (COUNT with HAVING)
9. Maintenance Status Rooms (FILTERING)
10. Staff Salary Distribution (Complex calculation)


IMPLEMENTATION NOTES
================================================================================

MySQL-Only Features Used:
✓ AUTO_INCREMENT (not SERIAL from PostgreSQL)
✓ DECIMAL for currency (not MONEY type)
✓ DATEDIFF() function
✓ ON DELETE CASCADE
✓ Standard MySQL functions (COUNT, SUM, AVG, etc.)

NOT Used (PostgreSQL Specific):
✗ SERIAL type
✗ uuid
✗ RETURNING clause
✗ \c command
✗ PostgreSQL-specific syntax

All table and column names are lowercase (consistency requirement).


EXECUTION INSTRUCTIONS
================================================================================

1. Load Schema:
   mysql -u root -p < ddl.sql

2. Load Sample Data:
   mysql -u root -p view_lab < seed.sql

3. Run Queries:
   mysql -u root -p view_lab < queries.sql

4. Direct Query Testing:
   mysql -u root -p
   use view_lab;
   SELECT * FROM guests;


FUTURE ENHANCEMENTS
================================================================================
- Add payment_method and payment_status to bookings
- Add room service charges table
- Implement guest preferences table
- Add invoicing and billing tables
- Create stored procedures for complex operations
- Implement triggers for status updates
- Add activity logging table


CONSISTENCY GUARANTEES
================================================================================
✓ All semicolons properly placed
✓ No syntax errors in MySQL 8.0+
✓ Consistent lowercase naming convention
✓ All queries tested for MySQL compatibility
✓ Foreign key relationships validated
✓ Sample data realistic and consistent


*/

-- This is a documentation file. Execute ddl.sql, seed.sql, and queries.sql
-- separately to set up and test the Hotel Management System database.
