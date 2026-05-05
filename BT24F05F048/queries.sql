-- 1. Patient with doctor
SELECT p.name, d.name AS doctor
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;

-- 2. Total bill per patient
SELECT p.name, SUM(b.total_amount) AS total_bill
FROM patients p
JOIN appointments a ON p.patient_id = a.patient_id
JOIN treatments t ON a.appointment_id = t.appointment_id
JOIN bills b ON t.treatment_id = b.treatment_id
GROUP BY p.name;

-- 3. Doctors with more than 1 appointment
SELECT d.name, COUNT(*) AS total
FROM doctors d
JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.name
HAVING COUNT(*) > 1;

-- 4. Expensive treatments
SELECT * FROM treatments WHERE cost > 3000;

-- 5. Paid bills
SELECT * FROM bills WHERE payment_status = 'Paid';
