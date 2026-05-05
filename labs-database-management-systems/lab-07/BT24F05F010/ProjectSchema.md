# Hostel Management System - Schema

## Problem Statement
A hostel needs to track student allocations, room assignments, and bill payments.

---

## Tables

### hostels
Hostel buildings
- **hostel_id**: PK (int)
- **hostel_name**: Name (varchar)
- **address**: Location (varchar)
- **total_rooms**: Room count (int)

### rooms
Physical rooms
- **room_id**: PK (int)
- **hostel_id**: FK → hostels
- **room_number**: Identifier (varchar)
- **capacity**: Bed count (int)
- **status**: Available/Occupied (varchar)

### students
Student residents
- **student_id**: PK (int)
- **name**: Full name (varchar)
- **email**: Contact (varchar)
- **phone**: Phone (varchar)
- **enrollment_date**: Join date (date)

### allocations
Room assignments
- **allocation_id**: PK (int)
- **room_id**: FK → rooms
- **student_id**: FK → students
- **check_in_date**: Move-in date (date)
- **check_out_date**: Move-out date (date)
- **status**: Active/Completed (varchar)

### bills
Fees and payments
- **bill_id**: PK (int)
- **student_id**: FK → students
- **allocation_id**: FK → allocations
- **amount**: Fee amount (decimal)
- **bill_date**: Bill date (date)
- **status**: Pending/Paid (varchar)

---

## Relationships
```
hostels (1) ──→ (N) rooms
                   ↓
            allocations ←─ (1) students
                   ↓
                 bills
```

## Normalization
- **1NF**: Atomic attributes only
- **2NF**: No partial dependencies
- **3NF**: No transitive dependencies
- All FK constraints enforced ✓

