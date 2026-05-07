# Hospital Database Project Report

## Project Overview
This mini-project implements a simple hospital management database system. The database tracks departments, doctors, patients, and their appointments.

## Requirements Analysis
The system needs to manage:
- Hospital departments and their locations
- Doctors and their specializations, assigned to departments
- Patient information
- Appointment scheduling between patients and doctors

## Database Design
### Entity-Relationship Model
- **Department**: Central entity for hospital organization
- **Doctor**: Employees assigned to departments
- **Patient**: Individuals receiving care
- **Appointment**: Junction entity linking patients and doctors with scheduling details

### Normalization Decisions
- Used 3NF to eliminate redundancy and ensure data integrity
- Composite keys avoided in favor of surrogate keys for simplicity
- Foreign key constraints ensure referential integrity
- ON DELETE CASCADE for appointments (delete related appointments if patient/doctor is removed)
- ON DELETE SET NULL for doctors (keep doctor record if department is deleted)

## Implementation
### DDL (ddl.sql)
- Created tables with appropriate data types
- Primary keys using SERIAL for auto-increment
- Foreign key relationships with referential actions

### Seed Data (seed.sql)
- Sample data for 3 departments, 4 doctors, 4 patients, and 5 appointments
- Realistic but fictional data for testing

### Queries (queries.sql)
- Basic CRUD operations
- JOIN queries for related data
- Aggregate queries for reporting
- Filtered queries for specific use cases

## Testing
The database was tested using PostgreSQL:
1. Created database schema
2. Inserted sample data
3. Ran queries to verify functionality
4. Checked referential integrity constraints

## Future Enhancements
Potential additions could include:
- Medical records/treatments
- Billing/invoices
- Staff roles beyond doctors
- Room/bed assignments
- Insurance information

## Conclusion
This simple hospital database provides a foundation for managing basic hospital operations. The design is normalized, scalable, and follows database best practices.