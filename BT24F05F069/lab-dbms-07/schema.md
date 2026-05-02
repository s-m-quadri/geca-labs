# Database Schema: Clinic Management System

## Entities and Attributes
1. **Specializations**: Stores medical departments.
   - `spec_id` (PK): Unique ID for the specialty.
   - `spec_name`: Name of the department (e.g., Cardiology).
   
2. **Doctors**: Stores healthcare provider details.
   - `doc_id` (PK): Unique ID for the doctor.
   - `doc_name`: Full name of the doctor.
   - `spec_id` (FK): Links to the Specializations table.

3. **Patients**: Stores visitor information.
   - `pat_id` (PK): Unique ID for the patient.
   - `pat_name`: Name of the patient.
   - `email`: Contact information.

4. **Appointments**: The junction table linking doctors and patients.
   - `appt_id` (PK): Unique ID for the visit.
   - `doc_id` (FK): The doctor assigned.
   - `pat_id` (FK): The patient visiting.
   - `appt_date`: Date of the appointment.

## Relationships and Cardinality
- **Specializations to Doctors (1:N)**: One specialization can have many doctors, but a doctor belongs to one specialization.
- **Doctors to Appointments (1:N)**: One doctor can have multiple appointments.
- **Patients to Appointments (1:N)**: One patient can book multiple appointments over time.
- **Chain of Foreign Keys**: Specializations → Doctors → Appointments.