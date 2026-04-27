-- ============================================================
-- Lab 7: Hospital Management System
-- queries.sql - Non-trivial Query Set (10 queries)
-- ============================================================

\c hospital_db;

-- ============================================================
-- Q1. MULTI-TABLE JOIN
-- Full appointment detail: patient name, doctor name,
-- department, date, and status
-- ============================================================
SELECT
    p.first_name || ' ' || p.last_name         AS patient,
    d.first_name || ' ' || d.last_name         AS doctor,
    d.speciality,
    dep.dept_name                               AS department,
    a.appt_date,
    a.appt_time,
    a.status
FROM appointment a
JOIN patient    p   ON p.patient_id = a.patient_id
JOIN doctor     d   ON d.doctor_id  = a.doctor_id
JOIN department dep ON dep.dept_id  = d.dept_id
ORDER BY a.appt_date;


-- ============================================================
-- Q2. AGGREGATE + GROUP BY
-- Total revenue collected (paid bills) per department,
-- sorted highest first
-- ============================================================
SELECT
    dep.dept_name,
    COUNT(b.bill_id)           AS total_bills,
    SUM(b.amount)              AS total_billed,
    SUM(CASE WHEN b.paid THEN b.amount ELSE 0 END) AS total_collected,
    SUM(CASE WHEN NOT b.paid THEN b.amount ELSE 0 END) AS outstanding
FROM bill b
JOIN appointment a   ON a.appt_id  = b.appt_id
JOIN doctor      d   ON d.doctor_id = a.doctor_id
JOIN department  dep ON dep.dept_id = d.dept_id
GROUP BY dep.dept_name
ORDER BY total_billed DESC;


-- ============================================================
-- Q3. HAVING CLAUSE
-- Doctors who have seen MORE THAN 1 patient
-- (i.e., more than one completed appointment)
-- ============================================================
SELECT
    d.first_name || ' ' || d.last_name AS doctor,
    d.speciality,
    COUNT(a.appt_id)                   AS appointments_count
FROM doctor d
JOIN appointment a ON a.doctor_id = d.doctor_id
WHERE a.status = 'Completed'
GROUP BY d.doctor_id, d.first_name, d.last_name, d.speciality
HAVING COUNT(a.appt_id) > 1
ORDER BY appointments_count DESC;


-- ============================================================
-- Q4. CREATE VIEW — doctor workload summary
-- ============================================================
CREATE OR REPLACE VIEW vw_doctor_workload AS
SELECT
    d.doctor_id,
    d.first_name || ' ' || d.last_name AS doctor_name,
    d.speciality,
    dep.dept_name,
    COUNT(a.appt_id)                   AS total_appointments,
    SUM(CASE WHEN a.status = 'Completed' THEN 1 ELSE 0 END) AS completed,
    SUM(CASE WHEN a.status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM doctor d
JOIN department dep ON dep.dept_id  = d.dept_id
LEFT JOIN appointment a ON a.doctor_id = d.doctor_id
GROUP BY d.doctor_id, d.first_name, d.last_name, d.speciality, dep.dept_name;

-- Query against the view
SELECT * FROM vw_doctor_workload ORDER BY total_appointments DESC;


-- ============================================================
-- Q5. SUBQUERY
-- Business Question: Which patients have at least one SEVERE diagnosis?
-- ============================================================
-- Business Question: List all patients who have been diagnosed with
-- a SEVERE or CRITICAL condition, along with the disease description.
SELECT DISTINCT
    p.first_name || ' ' || p.last_name AS patient,
    p.phone,
    di.description                     AS diagnosis,
    di.severity
FROM patient p
WHERE p.patient_id IN (
    SELECT a.patient_id
    FROM appointment a
    JOIN diagnosis di ON di.appt_id = a.appt_id
    WHERE di.severity IN ('Severe', 'Critical')
)
JOIN appointment a  ON a.patient_id  = p.patient_id
JOIN diagnosis   di ON di.appt_id    = a.appt_id
WHERE di.severity IN ('Severe', 'Critical')
ORDER BY p.last_name;


-- ============================================================
-- Q6. MULTI-JOIN + FILTER
-- Business Question: What medicines were prescribed for
-- Cardiology patients in the last 6 months?
-- ============================================================
SELECT
    p.first_name || ' ' || p.last_name AS patient,
    dep.dept_name                       AS department,
    rx.medicine,
    rx.dosage,
    rx.duration_days,
    a.appt_date
FROM prescription rx
JOIN appointment a   ON a.appt_id  = rx.appt_id
JOIN patient     p   ON p.patient_id = a.patient_id
JOIN doctor      d   ON d.doctor_id  = a.doctor_id
JOIN department  dep ON dep.dept_id  = d.dept_id
WHERE dep.dept_name = 'Cardiology'
  AND a.appt_date >= CURRENT_DATE - INTERVAL '6 months'
ORDER BY a.appt_date, rx.medicine;


-- ============================================================
-- Q7. AGGREGATE — Outstanding dues per patient
-- Business Question: Which patients still owe money?
-- ============================================================
SELECT
    p.first_name || ' ' || p.last_name AS patient,
    p.phone,
    SUM(b.amount)                       AS total_billed,
    SUM(CASE WHEN NOT b.paid THEN b.amount ELSE 0 END) AS amount_due
FROM patient p
JOIN appointment a ON a.patient_id = p.patient_id
JOIN bill        b ON b.appt_id    = a.appt_id
GROUP BY p.patient_id, p.first_name, p.last_name, p.phone
HAVING SUM(CASE WHEN NOT b.paid THEN b.amount ELSE 0 END) > 0
ORDER BY amount_due DESC;


-- ============================================================
-- Q8. CORRELATED SUBQUERY
-- Find appointments where the bill is ABOVE the average bill
-- amount for that doctor's department
-- ============================================================
SELECT
    a.appt_id,
    p.first_name || ' ' || p.last_name AS patient,
    dep.dept_name,
    b.amount                            AS bill_amount,
    ROUND(avg_dept.avg_bill, 2)         AS dept_avg_bill
FROM appointment a
JOIN patient    p   ON p.patient_id = a.patient_id
JOIN doctor     d   ON d.doctor_id  = a.doctor_id
JOIN department dep ON dep.dept_id  = d.dept_id
JOIN bill       b   ON b.appt_id    = a.appt_id
JOIN (
    SELECT d2.dept_id, AVG(b2.amount) AS avg_bill
    FROM bill b2
    JOIN appointment a2 ON a2.appt_id  = b2.appt_id
    JOIN doctor      d2 ON d2.doctor_id = a2.doctor_id
    GROUP BY d2.dept_id
) avg_dept ON avg_dept.dept_id = d.dept_id
WHERE b.amount > avg_dept.avg_bill
ORDER BY b.amount DESC;


-- ============================================================
-- Q9. DATE FUNCTION + AGGREGATE
-- Business Question: How many appointments are there per month?
-- ============================================================
SELECT
    TO_CHAR(appt_date, 'YYYY-MM') AS month,
    COUNT(*)                       AS total_appointments,
    SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed,
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled,
    SUM(CASE WHEN status = 'Scheduled' THEN 1 ELSE 0 END) AS scheduled
FROM appointment
GROUP BY TO_CHAR(appt_date, 'YYYY-MM')
ORDER BY month;


-- ============================================================
-- Q10. CHAIN JOIN (appointment → diagnosis + prescription)
-- Business Question: For each diagnosis, how many medicines
-- were prescribed, and what was the total prescription duration?
-- ============================================================
SELECT
    di.icd_code,
    di.description                           AS diagnosis,
    di.severity,
    COUNT(rx.rx_id)                          AS num_medicines,
    COALESCE(SUM(rx.duration_days), 0)       AS total_duration_days,
    ROUND(COALESCE(AVG(rx.duration_days),0), 1) AS avg_duration_days
FROM diagnosis di
LEFT JOIN prescription rx ON rx.appt_id = di.appt_id
GROUP BY di.diag_id, di.icd_code, di.description, di.severity
ORDER BY num_medicines DESC, di.severity;