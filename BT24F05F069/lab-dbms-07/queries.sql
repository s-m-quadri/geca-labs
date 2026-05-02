USE clinic_db;

SELECT 
    s.spec_name AS specialization,
    COUNT(d.doc_id) AS doctor_count,
    ROUND(AVG(CHAR_LENGTH(d.doc_name)), 2) AS avg_name_length
FROM specializations s
LEFT JOIN doctors d ON s.spec_id = d.spec_id
GROUP BY s.spec_id, s.spec_name
HAVING COUNT(d.doc_id) > 0
ORDER BY doctor_count DESC;


-- Query 1: Using the View (Requirement: SELECT from a view)
SELECT * FROM v_doctor_directory WHERE spec_name = 'Cardiology';

-- Query 2: Subquery Filter (Requirement: Subquery)
SELECT doc_name FROM doctors
WHERE spec_id IN (SELECT spec_id FROM specializations WHERE spec_name LIKE 'C%');

-- 3. Multi-table Join with Aggregate (Requirement: Join + GROUP BY)
-- Goal: Count how many doctors are in each specialization.
SELECT s.spec_name, COUNT(d.doc_id) AS total_doctors
FROM specializations s
LEFT JOIN doctors d ON s.spec_id = d.spec_id
GROUP BY s.spec_name;

-- 4. Aggregate with HAVING (Requirement: Meaningful aggregate)
-- Goal: Find specializations that have more than 2 doctors.
SELECT s.spec_name, COUNT(d.doc_id) AS doc_count
FROM specializations s
JOIN doctors d ON s.spec_id = d.spec_id
GROUP BY s.spec_name
HAVING COUNT(d.doc_id) > 2;

-- 5. Business Question: Who is the most senior doctor?
-- Goal: Finding a single record using ORDER BY and LIMIT.
SELECT doc_name 
FROM doctors 
ORDER BY doc_id ASC 
LIMIT 1;

-- 6. Pattern Matching (Requirement: Business question in plain English)
-- Goal: List all doctors whose names start with 'Dr. A'.
SELECT doc_name 
FROM doctors 
WHERE doc_name LIKE 'Dr. A%';

-- 7. Join with Ordering
-- Goal: List doctors and their specializations, sorted alphabetically by specialization.
SELECT d.doc_name, s.spec_name
FROM doctors d
JOIN specializations s ON d.spec_id = s.spec_id
ORDER BY s.spec_name ASC;

-- 8. Null Check (Requirement: Non-trivial logic)
-- Goal: Find specializations that currently have NO doctors assigned.
SELECT s.spec_name
FROM specializations s
LEFT JOIN doctors d ON s.spec_id = d.spec_id
WHERE d.doc_id IS NULL;