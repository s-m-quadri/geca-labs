# Relational DB Mini-Project: Hotel Booking

### 1. Concept
This project models a relational database for a hotel using MySQL. It handles core entities like guests, staff, rooms, and bookings, demonstrating how relational mapping works in practical software.

### 2. Entities Used
- `department` & `staff`: Tracks internal employees.
- `guest`: Customer directory.
- `room_type` & `room`: Maps out the physical hotel layout.
- `reservation` & `billing`: Connects customers to rooms and tracks financials.

### 3. Usage Guide
Run the scripts in order: `ddl.sql` -> `seed.sql` -> `queries.sql`. 

### 4. Learning Outcomes
This setup helped solidify concepts regarding Foreign Keys, Data Normalization, and complex `JOIN` queries to aggregate billing data across multiple normalized tables.