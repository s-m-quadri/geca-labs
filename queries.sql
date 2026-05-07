-- ==========================================
-- SYSTEM QUERIES
-- ==========================================
USE hospital_db;

-- Q1: Fetch all patient records
SELECT * FROM Patient;

-- Q2: Get doctors and their respective departments
SELECT doc.doctor_id, doc.name AS doctor_name, doc.specialization, dept.dept_name
FROM Doctor doc
INNER JOIN Department dept ON doc.dept_id = dept.dept_id;

-- Q3: Comprehensive appointment details
SELECT appt.appt_id, pat.name AS patient_name, doc.name AS doctor_name, appt.appt_date, appt.reason, appt.status
FROM Appointment appt
INNER JOIN Patient pat ON appt.patient_id = pat.patient_id
INNER JOIN Doctor doc ON appt.doctor_id = doc.doctor_id;

-- Q4: Filter for pending payments
SELECT b.bill_id, p.name AS patient_name, b.amount, b.bill_date
FROM Bill b
INNER JOIN Patient p ON b.patient_id = p.patient_id
WHERE b.paid = 'No';

-- Q5: Count unique patients per department
SELECT dept.dept_name, COUNT(DISTINCT appt.patient_id) AS total_patients
FROM Appointment appt
INNER JOIN Doctor doc ON appt.doctor_id = doc.doctor_id
INNER JOIN Department dept ON doc.dept_id = dept.dept_id
GROUP BY dept.dept_name;

-- Q6: Appointment history for patient ID 1 (Ravi Sharma)
SELECT appt.appt_date, doc.name AS doctor_name, appt.reason, appt.status
FROM Appointment appt
INNER JOIN Doctor doc ON appt.doctor_id = doc.doctor_id
WHERE appt.patient_id = 1;

-- Q7: Calculate total realized revenue
SELECT SUM(amount) AS total_revenue_collected FROM Bill WHERE paid = 'Yes';

-- Q8: Identify doctors handling 2 or more appointments
SELECT doc.name AS doctor_name, COUNT(appt.appt_id) AS total_appointments
FROM Appointment appt
INNER JOIN Doctor doc ON appt.doctor_id = doc.doctor_id
GROUP BY doc.doctor_id, doc.name
HAVING COUNT(appt.appt_id) >= 2;

-- Q9: Filter upcoming appointments
SELECT pat.name AS patient_name, doc.name AS doctor_name, appt.appt_date, appt.reason
FROM Appointment appt
INNER JOIN Patient pat ON appt.patient_id = pat.patient_id
INNER JOIN Doctor doc ON appt.doctor_id = doc.doctor_id
WHERE appt.status = 'Scheduled';

-- Q10: Financial summary grouped by patient
SELECT 
    pat.name AS patient_name, 
    COUNT(b.bill_id) AS total_visits, 
    SUM(b.amount) AS total_billed, 
    SUM(CASE WHEN b.paid = 'Yes' THEN b.amount ELSE 0 END) AS amount_paid
FROM Bill b
INNER JOIN Patient pat ON b.patient_id = pat.patient_id
GROUP BY pat.patient_id, pat.name;