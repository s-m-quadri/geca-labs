-- Hospital Management System
-- Queries File

USE hospital_db;


-- Query 1: List all patients

SELECT * FROM Patient;


-- Query 2: List all doctors with their department

SELECT 
    d.doctor_id,
    d.name          AS doctor_name,
    d.specialization,
    dep.dept_name
FROM Doctor d
JOIN Department dep ON d.dept_id = dep.dept_id;


-- Query 3: View all appointments with patient and doctor names

SELECT 
    a.appt_id,
    p.name      AS patient_name,
    d.name      AS doctor_name,
    a.appt_date,
    a.reason,
    a.status
FROM Appointment a
JOIN Patient p ON a.patient_id = p.patient_id
JOIN Doctor  d ON a.doctor_id  = d.doctor_id;


-- Query 4: Show all unpaid bills

SELECT 
    b.bill_id,
    p.name      AS patient_name,
    b.amount,
    b.bill_date
FROM Bill b
JOIN Patient p ON b.patient_id = p.patient_id
WHERE b.paid = 'No';


-- Query 5: Count patients per department (via appointments)

SELECT 
    dep.dept_name,
    COUNT(DISTINCT a.patient_id) AS total_patients
FROM Appointment a
JOIN Doctor     d   ON a.doctor_id = d.doctor_id
JOIN Department dep ON d.dept_id   = dep.dept_id
GROUP BY dep.dept_name;


-- Query 6: Find all appointments of a specific patient (Ravi Sharma)

SELECT 
    a.appt_date,
    d.name      AS doctor_name,
    a.reason,
    a.status
FROM Appointment a
JOIN Doctor d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 1;


-- Query 7: Total revenue collected (paid bills only)

SELECT 
    SUM(amount) AS total_revenue_collected
FROM Bill
WHERE paid = 'Yes';


-- Query 8: List doctors who have at least 2 appointments

SELECT 
    d.name          AS doctor_name,
    COUNT(a.appt_id) AS total_appointments
FROM Appointment a
JOIN Doctor d ON a.doctor_id = d.doctor_id
GROUP BY d.doctor_id, d.name
HAVING COUNT(a.appt_id) >= 2;


-- Query 9: Show all scheduled (upcoming) appointments

SELECT 
    p.name      AS patient_name,
    d.name      AS doctor_name,
    a.appt_date,
    a.reason
FROM Appointment a
JOIN Patient p ON a.patient_id = p.patient_id
JOIN Doctor  d ON a.doctor_id  = d.doctor_id
WHERE a.status = 'Scheduled';


-- Query 10: Get billing summary per patient

SELECT 
    p.name          AS patient_name,
    COUNT(b.bill_id) AS total_visits,
    SUM(b.amount)    AS total_billed,
    SUM(CASE WHEN b.paid = 'Yes' THEN b.amount ELSE 0 END) AS amount_paid
FROM Bill b
JOIN Patient p ON b.patient_id = p.patient_id
GROUP BY p.patient_id, p.name;