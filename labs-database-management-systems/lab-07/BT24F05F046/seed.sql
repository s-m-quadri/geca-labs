/* Seeding Data into the Hospital Database */
USE hospital_db;

-- Inserting into Department
INSERT INTO Department (dept_name, location) VALUES ('Cardiology', 'Block A, Floor 1');
INSERT INTO Department (dept_name, location) VALUES ('Neurology', 'Block B, Floor 2');
INSERT INTO Department (dept_name, location) VALUES ('Orthopedics', 'Block A, Floor 3');
INSERT INTO Department (dept_name, location) VALUES ('General Medicine', 'Block C, Floor 1');
INSERT INTO Department (dept_name, location) VALUES ('Pediatrics', 'Block D, Floor 2');

-- Inserting into Doctor
INSERT INTO Doctor (name, specialization, phone, dept_id) VALUES ('Dr. Ramesh Gupta', 'Heart Specialist', '9876543210', 1);
INSERT INTO Doctor (name, specialization, phone, dept_id) VALUES ('Dr. Priya Mehta', 'Brain & Nerves', '9876543211', 2);
INSERT INTO Doctor (name, specialization, phone, dept_id) VALUES ('Dr. Arjun Patil', 'Bone Specialist', '9876543212', 3);
INSERT INTO Doctor (name, specialization, phone, dept_id) VALUES ('Dr. Sneha Kulkarni', 'General Physician', '9876543213', 4);
INSERT INTO Doctor (name, specialization, phone, dept_id) VALUES ('Dr. Vikram Joshi', 'Child Specialist', '9876543214', 5);

-- Inserting into Patient
INSERT INTO Patient (name, age, gender, phone, address) VALUES ('Ravi Sharma', 35, 'Male', '9001234567', 'Solapur, MH');
INSERT INTO Patient (name, age, gender, phone, address) VALUES ('Anita Desai', 28, 'Female', '9001234568', 'Pune, MH');
INSERT INTO Patient (name, age, gender, phone, address) VALUES ('Suresh Nair', 52, 'Male', '9001234569', 'Kolhapur, MH');
INSERT INTO Patient (name, age, gender, phone, address) VALUES ('Pooja Reddy', 22, 'Female', '9001234570', 'Latur, MH');
INSERT INTO Patient (name, age, gender, phone, address) VALUES ('Manoj Yadav', 45, 'Male', '9001234571', 'Nagpur, MH');
INSERT INTO Patient (name, age, gender, phone, address) VALUES ('Kavita Singh', 60, 'Female', '9001234572', 'Solapur, MH');

-- Inserting into Appointment
INSERT INTO Appointment (patient_id, doctor_id, appt_date, reason, status) VALUES 
(1, 1, '2026-04-01', 'Chest Pain', 'Completed'),
(2, 2, '2026-04-02', 'Frequent Headaches', 'Completed'),
(3, 3, '2026-04-03', 'Knee Pain', 'Completed'),
(4, 4, '2026-04-05', 'Fever and Cold', 'Completed'),
(5, 1, '2026-04-10', 'Heart Checkup', 'Completed'),
(6, 5, '2026-04-12', 'Child Vaccination', 'Scheduled'),
(1, 4, '2026-04-15', 'Follow-up Visit', 'Scheduled');

-- Inserting into Bill
INSERT INTO Bill (patient_id, appt_id, amount, paid, bill_date) VALUES 
(1, 1, 1500.00, 'Yes', '2026-04-01'),
(2, 2, 1200.00, 'Yes', '2026-04-02'),
(3, 3, 2000.00, 'No', '2026-04-03'),
(4, 4, 800.00, 'Yes', '2026-04-05'),
(5, 5, 1500.00, 'No', '2026-04-10'),
(6, 6, 500.00, 'No', '2026-04-12');