-- Seed Data - Sample records for testing

USE hotel_db;

-- Departments
INSERT INTO Departments (dept_name, manager) VALUES
('Front Desk',   'Amit Kulkarni'),
('Housekeeping', 'Neha Jadhav'),
('Maintenance',  'Prakash Nair');

-- Staff
INSERT INTO Staff (dept_id, name, role, phone, salary) VALUES
(1, 'Riya Singh',     'Receptionist', '9811111111', 34000),
(1, 'Vikram Shah',    'Receptionist', '9811112222', 31000),
(2, 'Meena Pillai',   'Housekeeper',  '9811113333', 24000),
(3, 'Prakash Nair',   'Technician',   '9811114444', 37000);

-- Guests
INSERT INTO Guests (name, email, phone, address, id_proof) VALUES
('Rahul Verma',    'rahulv@email.com',   '9711111111', 'Nagpur',   'Aadhar-987654'),
('Divya Menon',    'divya@email.com',    '9711112222', 'Kochi',    'Passport-IN4567'),
('Karan Patil',    'karan@email.com',    '9711113333', 'Nashik',   'Aadhar-112233'),
('Pooja Sharma',   'pooja@email.com',    '9711114444', 'Jaipur',   'PAN-PQRS5678L'),
('Michael Thomas', 'michael@email.com',  '9711115555', 'New York', 'Passport-US7788');

-- Room Types
INSERT INTO RoomTypes (type_name, price_per_night, max_persons) VALUES
('Standard', 1800, 2),
('Deluxe',   4000, 2),
('Suite',    7500, 3);

-- Rooms
INSERT INTO Rooms (room_no, type_id, floor, status) VALUES
('103', 1, 1, 'Available'),
('104', 1, 1, 'Occupied'),
('203', 2, 2, 'Available'),
('204', 2, 2, 'Occupied'),
('303', 3, 3, 'Available'),
('304', 3, 3, 'Under Maintenance');

-- Reservations
INSERT INTO Reservations (guest_id, room_id, staff_id, check_in, check_out, status) VALUES
(1, 2, 1, '2024-05-20', '2024-05-23', 'Checked-Out'),
(2, 4, 2, '2024-06-10', '2024-06-13', 'Checked-Out'),
(3, 5, 1, '2024-07-03', '2024-07-07', 'Checked-In'),
(4, 1, 2, '2024-07-12', '2024-07-14', 'Confirmed'),
(5, 3, 1, '2024-07-20', '2024-07-24', 'Confirmed');

-- Billing (payment info merged here)
INSERT INTO Billing (res_id, room_charge, extra_charge, tax_percent, total, pay_method, pay_status) VALUES
(1,  5400,  600, 18,  7080, 'UPI',         'Paid'),
(2, 12000,  500, 18, 14750, 'Cash',        'Paid'),
(3, 30000,  400, 18, 35872, 'Credit Card', 'Paid'),
(4,  3600,  200, 18,  4484, 'Net Banking', 'Pending'),
(5, 16000,  700, 18, 19706, 'Debit Card',  'Pending');

-- Housekeeping
INSERT INTO Housekeeping (room_id, staff_id, task_type, task_date, status) VALUES
(2, 3, 'Cleaning',     '2024-05-21', 'Done'),
(4, 3, 'Linen Change', '2024-06-11', 'Done'),
(6, 4, 'Repair',       '2024-06-25', 'Done'),
(5, 3, 'Cleaning',     '2024-07-04', 'Pending'),
(1, 3, 'Inspection',   '2024-07-11', 'Pending');