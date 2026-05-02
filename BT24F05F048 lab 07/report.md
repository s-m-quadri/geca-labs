# Hospital Database Mini Project

## Problem
This project manages hospital data like patients, doctors, and appointments.

## Design
The database is divided into tables to avoid duplication.
Appointments connect patients and doctors.

## Sample Queries
- Display patient appointments
- Show doctor details
- Count total appointments

### Query Output
Running the join query to show patients and their doctors:

```
 name  |    name    
-------+------------
 Rahul | Dr. Sharma
 Priya | Dr. Mehta
(2 rows)
```

## Limitations
- No billing system
- No advanced patient history