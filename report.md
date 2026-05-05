# HMS (Hospital Management System) Database
---

## 1. Introduction

This repository contains a MySQL-based mini-project for a Hospital Management System. It is designed to act as a backend data store for tracking doctors, patient details, daily appointments, and financial billing.

The main learning outcome of this project was to get comfortable with relational database mechanics—specifically creating schemas, mapping relationships with foreign keys, and writing functional SQL scripts.

---

## 2. Project Goals

- Create a clean and logical table structure.
- Enforce data integrity using primary and foreign keys.
- Populate the tables with dummy data for testing.
- Extract useful insights using SQL (for example, finding out which doctor is the busiest, or filtering unpaid invoices).

---

## 3. Table Breakdown

Here are the five tables used to manage the hospital's data:

*   **Department:** Categorizes the hospital (e.g., Neurology, Pediatrics).
*   **Doctor:** Contains physician details, assigned to a specific Department.
*   **Patient:** Holds personal information for anyone admitted or visiting.
*   **Appointment:** Records the scheduling details when a Patient sees a Doctor.
*   **Bill:** Tracks the cost and payment status linked to specific appointments.

---

## 4. Directory Layout

```text
hospital_management/
│
├── ddl.sql          -- Initializes DB and table structures
├── seed.sql         -- Fills the tables with sample records
├── queries.sql      -- 10 executable SQL commands to test data
├── er_diagram.html  -- The database schema diagram
└── report.md        -- Project summary (this file)