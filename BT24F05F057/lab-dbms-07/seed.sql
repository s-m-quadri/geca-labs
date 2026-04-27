-- ============================================================
-- Lab 7: Hospital Management System
-- seed.sql - Realistic Sample Data
-- ============================================================

\c hospital_db;

-- -----------------------------------------------
-- DEPARTMENTS  (6 rows)
-- -----------------------------------------------
INSERT INTO department (dept_name, location, phone) VALUES
('Cardiology',        'Block A, Floor 2', '020-4411'),
('Neurology',         'Block B, Floor 1', '020-4422'),
('Orthopaedics',      'Block A, Floor 3', '020-4433'),
('General Medicine',  'Block C, Floor 1', '020-4444'),
('Paediatrics',       'Block D, Floor 1', '020-4455'),
('Dermatology',       'Block C, Floor 2', '020-4466');

-- -----------------------------------------------
-- DOCTORS  (10 rows)
-- -----------------------------------------------
INSERT INTO doctor (first_name, last_name, speciality, email, dept_id) VALUES
('Rohan',   'Desai',    'Interventional Cardiology', 'r.desai@hospital.in',    1),
('Priya',   'Kulkarni', 'Echocardiography',          'p.kulkarni@hospital.in', 1),
('Amit',    'Joshi',    'Stroke & Epilepsy',         'a.joshi@hospital.in',    2),
('Sneha',   'Patil',    'Neurodegenerative Disease', 's.patil@hospital.in',    2),
('Vikram',  'Shinde',   'Joint Replacement',         'v.shinde@hospital.in',   3),
('Meera',   'Nair',     'Sports Medicine',           'm.nair@hospital.in',     3),
('Suresh',  'Kumar',    'Internal Medicine',         's.kumar@hospital.in',    4),
('Anjali',  'Mehta',    'Diabetology',               'a.mehta@hospital.in',    4),
('Deepak',  'Rao',      'Child Development',         'd.rao@hospital.in',      5),
('Kavita',  'Singh',    'Acne & Eczema',             'k.singh@hospital.in',    6);

-- -----------------------------------------------
-- PATIENTS  (12 rows)
-- -----------------------------------------------
INSERT INTO patient (first_name, last_name, dob, gender, phone, address) VALUES
('Arjun',    'More',       '1985-03-14', 'M', '9890000001', 'Aurangabad'),
('Sarita',   'Chopra',     '1992-07-22', 'F', '9890000002', 'Pune'),
('Rajeev',   'Iyer',       '1968-11-05', 'M', '9890000003', 'Mumbai'),
('Priyanka', 'Sharma',     '2000-01-30', 'F', '9890000004', 'Nashik'),
('Mohit',    'Verma',      '1975-06-18', 'M', '9890000005', 'Nagpur'),
('Sunita',   'Gaikwad',    '1988-09-09', 'F', '9890000006', 'Aurangabad'),
('Ramesh',   'Bhat',       '1960-12-20', 'M', '9890000007', 'Solapur'),
('Kavita',   'Tiwari',     '1995-04-15', 'F', '9890000008', 'Jalgaon'),
('Nikhil',   'Deshmukh',   '2010-08-01', 'M', '9890000009', 'Aurangabad'),
('Leela',    'Shetty',     '1940-02-28', 'F', '9890000010', 'Kolhapur'),
('Aditya',   'Pandey',     '1999-11-11', 'M', '9890000011', 'Latur'),
('Anita',    'Kulkarni',   '1982-05-25', 'F', '9890000012', 'Pune');

-- -----------------------------------------------
-- APPOINTMENTS  (15 rows)
-- -----------------------------------------------
INSERT INTO appointment (patient_id, doctor_id, appt_date, appt_time, status, notes) VALUES
(1,  1, '2025-01-10', '09:00', 'Completed', 'Chest pain evaluation'),
(2,  7, '2025-01-12', '10:30', 'Completed', 'Routine check-up'),
(3,  3, '2025-01-15', '11:00', 'Completed', 'Headache and memory issues'),
(4,  8, '2025-01-20', '14:00', 'Completed', 'Diabetes management'),
(5,  5, '2025-01-22', '09:30', 'Completed', 'Knee pain assessment'),
(6,  1, '2025-02-01', '10:00', 'Completed', 'Follow-up angiography'),
(7,  4, '2025-02-05', '11:30', 'Completed', 'Tremor and gait issues'),
(8,  10,'2025-02-10', '15:00', 'Completed', 'Eczema on arms'),
(9,  9, '2025-02-14', '09:00', 'Completed', 'Child development screening'),
(10, 2, '2025-02-18', '13:00', 'Completed', 'Echocardiogram for elderly patient'),
(11, 6, '2025-03-01', '10:00', 'Cancelled', 'Sports injury -- cancelled by patient'),
(12, 7, '2025-03-05', '11:00', 'Completed', 'Fever and fatigue'),
(1,  2, '2025-03-10', '09:30', 'Completed', 'Echo follow-up'),
(3,  3, '2025-03-15', '10:00', 'Scheduled', 'MRI review appointment'),
(5,  5, '2025-03-20', '14:30', 'Scheduled', 'Pre-surgery knee assessment');

-- -----------------------------------------------
-- DIAGNOSES  (12 rows, skipping cancelled appt 11)
-- -----------------------------------------------
INSERT INTO diagnosis (appt_id, icd_code, description, severity) VALUES
(1,  'I20.9', 'Unstable Angina',               'Severe'),
(2,  'Z00.0', 'General Health Examination',    'Mild'),
(3,  'G43.9', 'Migraine without aura',         'Moderate'),
(4,  'E11.9', 'Type 2 Diabetes Mellitus',      'Moderate'),
(5,  'M17.1', 'Primary osteoarthritis of knee','Moderate'),
(6,  'I25.1', 'Atherosclerotic Heart Disease', 'Severe'),
(7,  'G20',   'Parkinsons Disease',            'Moderate'),
(8,  'L20.9', 'Atopic Dermatitis',             'Mild'),
(9,  'F84.0', 'Autism Spectrum Disorder',      'Moderate'),
(10, 'I50.9', 'Heart Failure, unspecified',    'Severe'),
(12, 'J11.1', 'Influenza with pneumonia',      'Moderate'),
(13, 'I42.9', 'Cardiomyopathy, unspecified',   'Severe');

-- -----------------------------------------------
-- PRESCRIPTIONS  (14 rows)
-- -----------------------------------------------
INSERT INTO prescription (appt_id, medicine, dosage, duration_days) VALUES
(1,  'Aspirin',         '75mg once daily',          90),
(1,  'Nitroglycerin',   '0.5mg SL PRN',             30),
(2,  'Multivitamin',    'One tablet daily',          30),
(3,  'Sumatriptan',     '50mg at onset of migraine', 10),
(4,  'Metformin',       '500mg twice daily',        180),
(4,  'Glimepiride',     '2mg before breakfast',     180),
(5,  'Ibuprofen',       '400mg thrice daily',        14),
(6,  'Atorvastatin',    '40mg once daily',           90),
(6,  'Clopidogrel',     '75mg once daily',           90),
(7,  'Levodopa',        '100mg thrice daily',       365),
(8,  'Tacrolimus cream','0.1% apply twice daily',    30),
(10, 'Furosemide',      '40mg once daily',           60),
(12, 'Azithromycin',    '500mg once daily',           5),
(13, 'Carvedilol',      '12.5mg twice daily',        90);

-- -----------------------------------------------
-- BILLS  (12 rows, only for completed appointments)
-- -----------------------------------------------
INSERT INTO bill (appt_id, amount, paid, payment_date) VALUES
(1,  3500.00, TRUE,  '2025-01-10'),
(2,   800.00, TRUE,  '2025-01-12'),
(3,  1200.00, TRUE,  '2025-01-15'),
(4,   900.00, TRUE,  '2025-01-20'),
(5,  1500.00, TRUE,  '2025-01-22'),
(6,  4200.00, FALSE, NULL),
(7,  1100.00, TRUE,  '2025-02-05'),
(8,   600.00, TRUE,  '2025-02-10'),
(9,   750.00, FALSE, NULL),
(10, 2800.00, TRUE,  '2025-02-18'),
(12,  700.00, TRUE,  '2025-03-05'),
(13, 1800.00, FALSE, NULL);