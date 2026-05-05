-- Defence Staff Management System - Sample Data (SEED)

USE defence_staff_mgmt;

-- Insert Ranks
INSERT INTO ranks (rank_name, seniority_level, description) VALUES
('Lieutenant General', 10, 'Senior commander rank'),
('Major General', 9, 'General officer rank'),
('Colonel', 8, 'Senior officer rank'),
('Major', 7, 'Middle officer rank'),
('Captain', 6, 'Junior officer rank'),
('Subedar', 5, 'Senior NCO rank'),
('Naib Subedar', 4, 'NCO rank'),
('Havildar', 3, 'Junior NCO rank'),
('Naik', 2, 'Senior soldier rank'),
('Sepoy', 1, 'Junior soldier rank');

-- Insert Departments
INSERT INTO departments (dept_name, description, location, head_count) VALUES
('Infantry Division', 'Ground combat and infantry operations', 'New Delhi', 450),
('Aviation Corp', 'Air operations and pilot training', 'Bangalore', 200),
('Intelligence Bureau', 'Intelligence gathering and analysis', 'New Delhi', 150),
('Signals Unit', 'Communication and signals management', 'Pune', 100),
('Medical Corps', 'Healthcare and medical services', 'Delhi Cantonment', 120),
('Logistics Division', 'Supply chain and logistics', 'Mumbai', 180);

-- Insert Qualifications
INSERT INTO qualifications (qual_name, description, renewal_months) VALUES
('Fighter Pilot Certification', 'Advanced pilot certification for combat aircraft', 24),
('Weapons Training Level 1', 'Basic weapons handling and safety', 12),
('Weapons Training Level 2', 'Advanced combat weapons training', 18),
('Medical Emergency Response', 'First aid and emergency medical response', 12),
('Signals Communication Expert', 'Expert-level communication systems training', 36),
('Intelligence Analysis', 'Intelligence gathering and analysis skills', 24),
('Leadership and Management', 'Officer leadership training program', 24),
('Cybersecurity Fundamentals', 'Basic cybersecurity awareness and protocols', 12);

-- Insert Staff (Main table)
INSERT INTO staff (title, first_name, last_name, date_of_birth, rank_id, dept_id, service_start_date, status) VALUES
('Col.', 'Rajesh', 'Kumar', '1968-05-15', 3, 1, '1988-06-01', 'active'),
('Maj.', 'Priya', 'Singh', '1975-03-22', 4, 2, '1995-09-15', 'active'),
('Capt.', 'Vikram', 'Patel', '1982-07-10', 5, 1, '2003-01-20', 'active'),
('Subedar', 'Arun', 'Sharma', '1980-11-05', 6, 1, '2001-02-10', 'active'),
('Havildar', 'Deepak', 'Gupta', '1985-09-18', 8, 2, '2006-08-12', 'active'),
('Naik', 'Suresh', 'Reddy', '1988-12-25', 9, 3, '2010-03-05', 'active'),
('Sepoy', 'Rohit', 'Verma', '1992-01-14', 10, 1, '2015-07-01', 'active'),
('Maj.', 'Anjali', 'Desai', '1978-06-30', 4, 3, '1996-11-15', 'active'),
('Capt.', 'Arjun', 'Nair', '1984-04-12', 5, 4, '2005-05-20', 'active'),
('Subedar', 'Vishal', 'Iyer', '1982-08-09', 6, 5, '2002-04-10', 'active'),
('Havildar', 'Mahesh', 'Rao', '1987-10-16', 8, 6, '2009-01-22', 'on_leave'),
('Naik', 'Karan', 'Bhat', '1990-03-28', 9, 2, '2012-06-11', 'active');

-- Insert Staff Qualifications (M:N relationship)
INSERT INTO staff_qualifications (staff_id, qual_id, acquired_date, expiry_date, certification_level) VALUES
-- Rajesh Kumar (Staff ID 1) qualifications
(1, 2, '2000-01-15', '2026-01-15', 'advanced'),
(1, 7, '2010-05-20', '2034-05-20', 'expert'),
-- Priya Singh (Staff ID 2) qualifications
(2, 1, '2000-06-10', '2026-06-10', 'expert'),
(2, 7, '2005-09-15', '2029-09-15', 'advanced'),
-- Vikram Patel (Staff ID 3) qualifications
(3, 2, '2005-03-10', '2026-03-10', 'intermediate'),
(3, 3, '2012-11-20', '2030-11-20', 'advanced'),
-- Arun Sharma (Staff ID 4) qualifications
(4, 2, '2008-02-14', '2025-02-14', 'basic'),
(4, 4, '2010-07-22', '2022-07-22', 'basic'),
-- Deepak Gupta (Staff ID 5) qualifications
(5, 1, '2006-08-12', '2032-08-12', 'advanced'),
(5, 7, '2015-03-10', '2039-03-10', 'intermediate'),
-- Suresh Reddy (Staff ID 6) qualifications
(6, 5, '2012-11-05', '2048-11-05', 'expert'),
(6, 8, '2022-01-12', '2025-01-12', 'basic'),
-- Rohit Verma (Staff ID 7) qualifications
(7, 2, '2016-02-10', '2028-02-10', 'basic'),
-- Anjali Desai (Staff ID 8) qualifications
(8, 6, '2010-04-20', '2034-04-20', 'advanced'),
(8, 7, '2015-09-10', '2039-09-10', 'advanced'),
-- Arjun Nair (Staff ID 9) qualifications
(9, 5, '2008-06-15', '2044-06-15', 'expert'),
-- Vishal Iyer (Staff ID 10) qualifications
(10, 4, '2010-02-18', '2022-02-18', 'intermediate'),
-- Mahesh Rao (Staff ID 11) qualifications
(11, 2, '2011-08-22', '2027-08-22', 'basic'),
-- Karan Bhat (Staff ID 12) qualifications
(12, 1, '2015-07-30', '2041-07-30', 'intermediate');

-- Insert Assignments
INSERT INTO assignments (staff_id, assignment_title, description, start_date, end_date, is_current, priority) VALUES
-- Current assignments
(1, 'Division Commander', 'In command of Infantry Division', '2020-01-15', NULL, TRUE, 'critical'),
(2, 'Flight Lead', 'Leading fighter squadron operations', '2021-06-10', NULL, TRUE, 'high'),
(3, 'Ground Operations Officer', 'Managing ground-level tactical operations', '2019-03-20', '2024-12-31', FALSE, 'high'),
(3, 'Operations Coordinator', 'Coordinating multi-unit operations', '2025-01-01', NULL, TRUE, 'high'),
(4, 'Training Commander', 'Overseeing infantry training programs', '2020-11-12', NULL, TRUE, 'medium'),
(5, 'Pilot-in-Command', 'Senior pilot for reconnaissance missions', '2018-02-05', NULL, TRUE, 'high'),
(6, 'Intelligence Analyst', 'Analyzing field intelligence reports', '2022-03-15', NULL, TRUE, 'critical'),
(7, 'Field Soldier', 'Active field operations personnel', '2023-08-01', NULL, TRUE, 'medium'),
(8, 'Counter-Intelligence Chief', 'Leading counter-intelligence operations', '2019-09-10', NULL, TRUE, 'critical'),
(9, 'Signals Officer', 'Managing communication infrastructure', '2021-05-22', NULL, TRUE, 'high'),
(10, 'Medical Officer-in-Charge', 'Head of medical operations', '2020-07-18', NULL, TRUE, 'critical'),
(11, 'Logistics Coordinator', 'Managing supply chain operations', '2022-01-05', NULL, TRUE, 'medium'),
(12, 'Pilot - Transport Aircraft', 'Flying transport and cargo missions', '2023-11-15', NULL, TRUE, 'high');

-- Insert Training Records
INSERT INTO training_records (staff_id, qual_id, training_type, completion_date, completion_percentage, trainer_name, notes) VALUES
(1, 2, 'formal', '2000-01-15', 95, 'Brigadier A. Verma', 'Excellent performance in live scenarios'),
(1, 7, 'formal', '2010-05-20', 98, 'Gen. M. Singh', 'Top of leadership batch'),
(2, 1, 'formal', '2000-06-10', 96, 'AVM Rajesh', 'High-performance combat pilot training'),
(2, 7, 'formal', '2005-09-15', 94, 'Lt. Gen. P. Nair', 'Strong leadership fundamentals'),
(3, 2, 'on_the_job', '2005-03-10', 92, 'Col. Rajesh Kumar', 'Field-based weapons training'),
(3, 3, 'formal', '2012-11-20', 89, 'Brigadier S. Rao', 'Advanced tactical weapons'),
(4, 2, 'workshop', '2008-02-14', 85, 'Maj. Vikram Patel', 'Hands-on weapons workshop'),
(4, 4, 'formal', '2010-07-22', 90, 'Dr. S. Patel', 'Emergency response certification'),
(5, 1, 'formal', '2006-08-12', 93, 'AVM Rajesh', 'Certification training for new aircraft'),
(5, 7, 'workshop', '2015-03-10', 87, 'Col. Kumar', 'Leadership development program'),
(6, 5, 'formal', '2012-11-05', 97, 'Brig. A. Mishra', 'Expert-level signals training'),
(6, 8, 'certification', '2022-01-12', 91, 'Dr. Cybersec', 'Cybersecurity certification exam'),
(7, 2, 'workshop', '2016-02-10', 80, 'Subedar Arun Sharma', 'Basic weapons safety and handling'),
(8, 6, 'formal', '2010-04-20', 95, 'Brigadier Intel', 'Advanced intelligence analysis'),
(8, 7, 'formal', '2015-09-10', 93, 'Gen. M. Singh', 'Senior leadership training'),
(9, 5, 'formal', '2008-06-15', 96, 'Brig. A. Mishra', 'Communication systems expert training'),
(10, 4, 'workshop', '2010-02-18', 88, 'Dr. Emergency', 'Medical emergency protocols'),
(11, 2, 'on_the_job', '2011-08-22', 82, 'Maj. Vikram Patel', 'Practical weapons training'),
(12, 1, 'certification', '2015-07-30', 94, 'Air Marshal X', 'Transport pilot certification');
