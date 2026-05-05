-- 1. Multi-table JOIN
SELECT p.name AS patient, d.name AS doctor, a.appointment_date
FROM patients p
JOIN appointments a ON p.patient_id = a.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id;

-- 2. GROUP BY + HAVING
SELECT doctor_id, COUNT(*) AS total_appointments
FROM appointments
GROUP BY doctor_id
HAVING COUNT(*) > 1;

-- 3. Subquery
SELECT name FROM patients
WHERE patient_id IN (
    SELECT patient_id FROM appointments
);

-- 4. VIEW
CREATE VIEW costly_treatments AS
SELECT * FROM treatments WHERE cost > 3000;

SELECT * FROM costly_treatments;

-- 5. Business Question
-- Which doctor has treated the most patients?
SELECT d.name, COUNT(*) AS total
FROM doctors d
JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.name
ORDER BY total DESC
LIMIT 1;

-- 6. Find all treatments above 2000
SELECT * FROM treatments WHERE cost > 2000;

-- 7. List patients with their diagnosis
SELECT p.name, t.diagnosis
FROM patients p
JOIN appointments a ON p.patient_id = a.patient_id
JOIN treatments t ON a.appointment_id = t.appointment_id;

-- 8. Count total patients
SELECT COUNT(*) FROM patients;

-- 9. Find appointments in February
SELECT * FROM appointments
WHERE MONTH(appointment_date) = 2;