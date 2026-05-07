# Hospital Database Schema

## Overview
This is a simple hospital management database with four main entities: Department, Doctor, Patient, and Appointment.

## Entities

### Department
- **dept_id**: Primary key, auto-increment
- **name**: Department name (unique)
- **location**: Building or location

### Doctor
- **doc_id**: Primary key, auto-increment
- **name**: Doctor's name
- **dept_id**: Foreign key to Department
- **specialization**: Doctor's specialty

### Patient
- **pat_id**: Primary key, auto-increment
- **name**: Patient's name
- **dob**: Date of birth
- **address**: Patient's address

### Appointment
- **appt_id**: Primary key, auto-increment
- **pat_id**: Foreign key to Patient
- **doc_id**: Foreign key to Doctor
- **appt_date**: Appointment date
- **appt_time**: Appointment time
- **reason**: Reason for appointment

## Relationships
- A Doctor belongs to one Department (many-to-one)
- A Patient can have multiple Appointments (one-to-many)
- A Doctor can have multiple Appointments (one-to-many)
- An Appointment links one Patient to one Doctor (many-to-one on both sides)

## Normalization
The schema is in 3NF:
- All attributes depend on the primary key
- No transitive dependencies
- Foreign keys properly reference primary keys