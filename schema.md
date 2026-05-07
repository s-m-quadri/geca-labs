 schema.md (write this in report)
* Description

The Hostel Management System is designed to manage student accommodation, fee records, and complaint handling in a structured relational database.

* Relationships
Hostel contains multiple Rooms (1:N)
Room contains multiple Students (1:N)
Student pays Fees (1:N)
Student raises Complaints (1:N)

* Design decisions
Separate Fee table avoids redundancy
Complaint table enables tracking issues independently
Foreign keys ensure data integrity