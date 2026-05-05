-- Doctors
INSERT INTO doctors (name, specialization) VALUES
('Dr. Sharma', 'Cardiologist'),
('Dr. Mehta', 'Dermatologist'),
('Dr. Patil', 'Orthopedic'),
('Dr. Khan', 'General Physician'),
('Dr. Singh', 'Neurologist'),
('Dr. Joshi', 'Pediatrician'),
('Dr. Gupta', 'ENT'),
('Dr. Reddy', 'Gynecologist');

-- Patients
INSERT INTO patients (name, age, gender) VALUES
('Amit', 25, 'Male'),
('Sneha', 30, 'Female'),
('Rahul', 40, 'Male'),
('Priya', 35, 'Female'),
('Rohan', 28, 'Male'),
('Anita', 50, 'Female'),
('Karan', 45, 'Male'),
('Pooja', 32, 'Female');

-- Appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date) VALUES
(1,1,'2026-01-01'),
(2,2,'2026-01-02'),
(3,3,'2026-01-03'),
(4,4,'2026-01-04'),
(5,5,'2026-01-05'),
(6,6,'2026-01-06'),
(7,7,'2026-01-07'),
(8,8,'2026-01-08'),
(1,2,'2026-02-01'),
(2,3,'2026-02-02');

-- Treatments
INSERT INTO treatments (appointment_id, diagnosis, cost) VALUES
(1,'Heart Checkup',5000),
(2,'Skin Allergy',1500),
(3,'Fracture',7000),
(4,'Fever',800),
(5,'Migraine',3000),
(6,'Child Checkup',1200),
(7,'Ear Infection',2000),
(8,'Pregnancy Check',4000),
(9,'Skin Rash',1800),
(10,'Bone Pain',3500);