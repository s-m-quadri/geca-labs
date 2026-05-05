INSERT INTO patients (name, age, gender, phone) VALUES
('Rahul', 25, 'Male', '9876543210'),
('Priya', 30, 'Female', '9876543211'),
('Amit', 40, 'Male', '9876543212');

INSERT INTO doctors (name, specialization, experience) VALUES
('Dr. Sharma', 'Cardiologist', 10),
('Dr. Mehta', 'Dermatologist', 8),
('Dr. Singh', 'Neurologist', 12);

INSERT INTO appointments (patient_id, doctor_id, appointment_date) VALUES
(1, 1, '2026-01-01'),
(2, 2, '2026-01-02'),
(3, 3, '2026-01-03');

INSERT INTO treatments (appointment_id, description, cost) VALUES
(1, 'Heart Checkup', 5000),
(2, 'Skin Treatment', 2000),
(3, 'Brain Scan', 7000);

INSERT INTO bills (treatment_id, total_amount, payment_status) VALUES
(1, 5000, 'Paid'),
(2, 2000, 'Pending'),
(3, 7000, 'Paid');