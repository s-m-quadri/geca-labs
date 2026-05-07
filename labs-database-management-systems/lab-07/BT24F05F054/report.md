# Database Project: Hospital Management System

## 1. Project Overview

This mini-project is a relational database designed for a Hospital Management System using MySQL. The core concept is to efficiently manage and store essential hospital data, including patient records, doctor profiles, departmental details, appointment schedules, and billing information. 

The primary focus of this project is to implement standard database principles: establishing tables, connecting them via foreign keys, populating them with mock data, and retrieving information through practical queries.

---

## 2. Main Objectives

- Architect a normalized database with interconnected tables.
- Correctly implement Primary and Foreign Key constraints.
- Seed the database with realistic sample records.
- Formulate SQL queries to solve practical scenarios (e.g., "Identify patients with pending payments" or "Count appointments per doctor").

---

## 3. Database Entities

The system revolves around five core tables:

1. **Department:** Maintains the different hospital wards/departments.
2. **Doctor:** Keeps doctor profiles and links them to their respective departments.
3. **Patient:** Stores the demographic and contact details of the patients.
4. **Appointment:** Acts as a bridge connecting a Patient to a Doctor for a specific date.
5. **Bill:** Manages the financial/payment records generated from appointments.

---

## 4. Project Files

```text
hospital_management/
│
├── ddl.sql         => Script to create the database and schema
├── seed.sql        => Script to inject dummy data into the tables
├── queries.sql     => Contains 10 practical queries with comments
├── er_diagram.html => Visual representation of the database
└── report.md       => This documentation file