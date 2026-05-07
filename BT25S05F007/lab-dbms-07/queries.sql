-- Sample Queries for Hospital Database

-- 1. List all departments
SELECT * FROM Department;

-- 2. List all doctors with their department names
SELECT d.doc_id, d.name AS doctor_name, dept.name AS department_name, d.specialization
FROM Doctor d
JOIN Department dept ON d.dept_id = dept.dept_id;

-- 3. List all patients
SELECT * FROM Patient;

-- 4. List appointments with patient and doctor names
SELECT a.appt_id, p.name AS patient_name, d.name AS doctor_name, a.appt_date, a.appt_time, a.reason
FROM Appointment a
JOIN Patient p ON a.pat_id = p.pat_id
JOIN Doctor d ON a.doc_id = d.doc_id
ORDER BY a.appt_date;

-- 5. Count appointments per doctor
SELECT d.name AS doctor_name, COUNT(a.appt_id) AS appointment_count
FROM Doctor d
LEFT JOIN Appointment a ON d.doc_id = a.doc_id
GROUP BY d.doc_id, d.name;

-- 6. Find patients with appointments in a specific department
SELECT DISTINCT p.name AS patient_name
FROM Patient p
JOIN Appointment a ON p.pat_id = a.pat_id
JOIN Doctor d ON a.doc_id = d.doc_id
JOIN Department dept ON d.dept_id = dept.dept_id
WHERE dept.name = 'Cardiology';