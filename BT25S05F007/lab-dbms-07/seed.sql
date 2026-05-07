-- Sample data for Hospital Database

-- Departments
INSERT INTO Department (name, location) VALUES
('Cardiology', 'Building A'),
('Neurology', 'Building B'),
('Orthopedics', 'Building C');

-- Doctors
INSERT INTO Doctor (name, dept_id, specialization) VALUES
('Dr. Smith', 1, 'Heart Specialist'),
('Dr. Johnson', 2, 'Brain Specialist'),
('Dr. Williams', 3, 'Bone Specialist'),
('Dr. Brown', 1, 'Cardiac Surgeon');

-- Patients
INSERT INTO Patient (name, dob, address) VALUES
('John Doe', '1980-05-15', '123 Main St'),
('Jane Smith', '1990-03-22', '456 Oak Ave'),
('Bob Johnson', '1975-11-10', '789 Pine Rd'),
('Alice Williams', '1985-07-08', '321 Elm St');

-- Appointments
INSERT INTO Appointment (pat_id, doc_id, appt_date, appt_time, reason) VALUES
(1, 1, '2023-10-01', '10:00:00', 'Checkup'),
(2, 2, '2023-10-02', '11:00:00', 'Headache'),
(3, 3, '2023-10-03', '14:00:00', 'Broken leg'),
(4, 1, '2023-10-04', '09:00:00', 'Heart pain'),
(1, 4, '2023-10-05', '15:00:00', 'Surgery consultation');