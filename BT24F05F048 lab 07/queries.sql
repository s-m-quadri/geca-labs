-- simple join
SELECT p.name AS patient_name, d.name AS doctor_name
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;