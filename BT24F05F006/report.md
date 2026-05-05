# Hospital Management System

## 1. Problem
This system is designed to manage hospital operations such as patient records, doctor details, appointments, and treatments.

Users:
- Hospital staff
- Doctors
- Admin

---

## 2. Design

Tables:
- Doctors
- Patients
- Appointments
- Treatments

Relationships:
- One doctor can have many appointments (1:N)
- One patient can have many appointments (1:N)
- One appointment has one treatment (1:1)

Normalization:
- Data redundancy is avoided
- Separate tables for doctors and patients

Foreign Key Chain:
Doctors → Appointments → Treatments

---

## 3. Sample Results

Example:
- Doctor with most patients identified
- Costly treatments listed
- Patient diagnosis report generated

---

## 4. Limitations

- No login/authentication system
- No billing module
- No emergency handling
- No real-time updates

---

## 5. Future Improvements

- Add billing system
- Add staff management
- Add online appointment booking

---

## 6. References

- MySQL Documentation
- Classroom Notes