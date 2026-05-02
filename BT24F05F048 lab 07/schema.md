# Hospital Database Schema

## Tables
- Patients: stores patient details
- Doctors: stores doctor details
- Appointments: connects patients and doctors

## Relationships
- One patient can have many appointments (1:N)
- One doctor can handle many appointments (1:N)

## Foreign Keys
- appointments.patient_id → patients.patient_id
- appointments.doctor_id → doctors.doctor_id