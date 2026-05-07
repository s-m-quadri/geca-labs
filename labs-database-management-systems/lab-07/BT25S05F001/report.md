# SQL Project: Booking System Database

### Introduction
A straightforward MySQL implementation for tracking hotel data. It manages employees, customers, room classes, and stays, providing an easy-to-query system for daily operations.

### Structure
- **Core Info**: `Departments`, `Employees`, `Customers`
- **Inventory**: `RoomClasses`, `HotelRooms`
- **Operations**: `Stays`, `Payments`

### Execution
Simply run `ddl.sql` to build the schema, insert the mock data with `seed.sql`, and test the logic using `queries.sql`.

### Reflection
Building this highlighted the importance of unique constraints (like `StayID` in the `Payments` table to prevent double billing) and how standardizing data types improves overall database reliability.