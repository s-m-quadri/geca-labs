# Hospital Management System


## 1. Introduction

This project is a mini database for a Hospital Management System made using MySQL. The idea is simple — to store and manage basic information about patients, doctors, departments, appointments, and bills in an organized way.

And the focus is on understanding how relational databases work — creating tables, linking them using foreign keys, inserting sample records, and writing useful queries.

---

## 2. Objective
(i have copied this fron claude for proper wording)

- Design a clean database with related tables
- Use primary keys and foreign keys properly
- Insert meaningful sample data
- Write queries that answer real-world questions like "who are the unpaid patients?" or "which doctor has the most appointments?"

---

## 3. Tables Used

The tables involved and their purpose is as follows,

1. Department   --> Stores hospital departments (Cardiology, etc.) 
2. Doctor       --> Stores doctor info linked to a department    
3. Patient      --> Stores patient personal details              
4. Appointment  --> Links a patient with a doctor for a visit    
5. Bill         --> Stores billing info for each appointment     

---

## 4. File Structure
(i have copied this fron claude for better view)
```
hospital_management/
│
├── ddl.sql        → Creates the database and tables
├── seed.sql       → Inserts sample data
├── queries.sql    → 10 SQL queries with explanations
├── er_diagram.html → Visual ER diagram
└── report.md      → This file
```

---

## 6. How to Run

To run this files first run ddl.sql then seed.sql and finally queries.sql
one need to go in ths specific order only else it wont work.

---

## 10. Conclusion

This project helped me understand how to design a simple but practical relational database. Using foreign keys makes sure the data stays connected and consistent. Writing JOIN queries showed me how powerful SQL can be when tables are linked properly.

The Hospital Management System is a good real-world example because it covers different types of relationships — one-to-many (department to doctors) and many-to-many-like (patients and doctors through appointments).