/* Executing SQL Queries */
USE hospital_db;

-- 1. Get every patient in the database
SELECT * FROM Patient;

-- 2. See doctors and what department they belong to
SELECT d.doctor_id, d.name doctor_name, d.specialization, dp.dept_name
FROM Doctor d
JOIN Department dp ON d.dept_id = dp.dept_id;

-- 3. Check appointments with full names attached
SELECT a.appt_id, p.name patient_name, d.name doctor_name, a.appt_date, a.reason, a.status
FROM Appointment a
JOIN Patient p ON a.patient_id = p.patient_id
JOIN Doctor d ON a.doctor_id = d.doctor_id;

-- 4. Find all bills that haven't been paid yet
SELECT b.bill_id, p.name patient_name, b.amount, b.bill_date
FROM Bill b
JOIN Patient p ON b.patient_id = p.patient_id
WHERE b.paid = 'No';

-- 5. See how many patients each department is getting
SELECT dp.dept_name, COUNT(DISTINCT a.patient_id) total_patients
FROM Appointment a
JOIN Doctor d ON a.doctor_id = d.doctor_id
JOIN Department dp ON d.dept_id = dp.dept_id
GROUP BY dp.dept_name;

-- 6. Pull all appointments for Ravi Sharma (patient 1)
SELECT a.appt_date, d.name doctor_name, a.reason, a.status
FROM Appointment a
JOIN Doctor d ON a.doctor_id = d.doctor_id
WHERE a.patient_id = 1;

-- 7. Total cash collected so far
SELECT SUM(amount) total_revenue_collected 
FROM Bill 
WHERE paid = 'Yes';

-- 8. Show doctors who have 2 or more appointments booked
SELECT d.name doctor_name, COUNT(a.appt_id) total_appointments
FROM Appointment a
JOIN Doctor d ON a.doctor_id = d.doctor_id
GROUP BY d.doctor_id, d.name
HAVING COUNT(a.appt_id) >= 2;

-- 9. Check upcoming appointments
SELECT p.name patient_name, d.name doctor_name, a.appt_date, a.reason
FROM Appointment a
JOIN Patient p ON a.patient_id = p.patient_id
JOIN Doctor d ON a.doctor_id = d.doctor_id
WHERE a.status = 'Scheduled';

-- 10. Patient billing breakdown
SELECT 
    p.name patient_name, 
    COUNT(b.bill_id) total_visits, 
    SUM(b.amount) total_billed, 
    SUM(CASE WHEN b.paid = 'Yes' THEN b.amount ELSE 0 END) amount_paid
FROM Bill b
JOIN Patient p ON b.patient_id = p.patient_id
GROUP BY p.patient_id, p.name;