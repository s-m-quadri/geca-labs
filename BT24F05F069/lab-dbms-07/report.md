# Project Report: Clinic Management System
**Author:** Pankaj (PRN: BT24F05F069)

## Problem Statement
Small clinics often struggle to track which doctors belong to which departments and manage patient schedules. This system provides a structured way to organize medical staff by specialization and track their appointments.

## Design Decisions
- **Normalization**: I separated 'Specializations' into its own table to avoid repeating department names (3NF). This ensures that if a department name changes, it only needs to be updated in one place.
- **Security/Abstraction**: I implemented a `v_doctor_directory` view to provide a public listing of doctors without exposing internal primary keys or sensitive contact data.

## Sample Results
| Specialization | Doctor Count | Avg Name Length |
| :--- | :--- | :--- |
| Cardiology | 2 | 14.50 |
| Neurology | 1 | 16.00 |

## Limitations and Future Scope
- **Current Limits**: The system does not currently track billing or medical prescriptions.
- **Future Improvements**: I would add a 'Bills' table and a Trigger to prevent booking two appointments for the same doctor at the same time.

## References
- MySQL Documentation for `AUTO_INCREMENT` and `JOIN` syntax.
- Lab 7 instruction manual.