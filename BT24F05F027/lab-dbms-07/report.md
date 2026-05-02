Hotel Management System


1. Introduction

This project is a mini database for a Hotel Management System made using MySQL. The idea is simple — to store and manage basic information about rooms, guests, staff, reservations, billing, and housekeeping in an organized way.

And the focus is on understanding how relational databases work — creating tables, linking them using foreign keys, inserting sample records, and writing useful queries.

2. Objective

Design a clean database with related tables
Use primary keys and foreign keys properly
Insert meaningful sample data
Write queries that answer real-world questions like "which rooms are available?" or "which guest has the highest bill?"

3. Tables Used

The tables involved and their purpose is as follows,

Department --> Stores hotel departments (Front Desk, Housekeeping, etc.)
Staff --> Stores employee info linked to a department
Guest --> Stores guest personal details
RoomType --> Stores room categories with pricing (Standard, Deluxe, Suite)
Room --> Stores individual room details and availability
Reservation --> Links a guest with a room for booking
Billing --> Stores billing info for each reservation
Housekeeping --> Stores cleaning/maintenance tasks assigned to staff

4. File Structure

hotel_management/
│
├── ddl.sql → Creates the database and tables
├── seed.sql → Inserts sample data
├── queries.sql → SQL queries with explanations
├── er_diagram.html → Visual ER diagram
└── report.md → This file

5. How to Run

To run this files first run ddl.sql then seed.sql and finally queries.sql one need to go in this specific order only else it wont work.

6. Conclusion

This project helped me understand how to design a simple but practical relational database. Using foreign keys makes sure the data stays connected and consistent. Writing JOIN queries showed me how powerful SQL can be when tables are linked properly.

The Hotel Management System is a good real-world example because it covers different types of relationships — one-to-many (department to staff, guest to reservations) and linked entities like guests and rooms through reservations.