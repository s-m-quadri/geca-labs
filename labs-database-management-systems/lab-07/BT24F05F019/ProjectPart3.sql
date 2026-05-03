-- View all patients
SELECT * FROM patients;

-- Join: patient + doctor + appointment
SELECT p.name AS patient, d.name AS doctor, a.appointment_date
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;

-- Count appointments per doctor
SELECT doctor_id, COUNT(*) AS total_appointments
FROM appointments
GROUP BY doctor_id;

-- Find unpaid bills
SELECT * FROM bills WHERE status = 'Pending';