
-- Seed Data - Sample records for testing

USE hotel_db;

-- Departments
INSERT INTO Departments (dept_name, manager) VALUES
('Front Desk',   'Rajesh Kumar'),
('Housekeeping', 'Sunita Sharma'),
('Maintenance',  'Suresh Patil');

-- Staff
INSERT INTO Staff (dept_id, name, role, phone, salary) VALUES
(1, 'Priya Joshi',  'Receptionist', '9800001111', 32000),
(1, 'Anil Mehta',   'Receptionist', '9800002222', 30000),
(2, 'Kavita Rao',   'Housekeeper',  '9800003333', 22000),
(3, 'Suresh Patil', 'Technician',   '9800004444', 35000);

-- Guests
INSERT INTO Guests (name, email, phone, address, id_proof) VALUES
('Arjun Desai',  'arjun@email.com',  '9700001111', 'Mumbai', 'Aadhar-123456'),
('Sneha Iyer',   'sneha@email.com',  '9700002222', 'Chennai','Passport-P1234'),
('Soham Joshi', 'soham@email.com',  '9700003333', 'Pune',   'Aadhar-654321'),
('Anjali Gupta', 'anjali@email.com', '9700004444', 'Delhi',  'PAN-ABCG1234D'),
('John Mathew',  'john@email.com',   '9700005555', 'London', 'Passport-UK9876');

-- Room Types
INSERT INTO RoomTypes (type_name, price_per_night, max_persons) VALUES
('Standard', 1500, 2),
('Deluxe',   3500, 2),
('Suite',    6000, 3);

-- Rooms
INSERT INTO Rooms (room_no, type_id, floor, status) VALUES
('101', 1, 1, 'Available'),
('102', 1, 1, 'Occupied'),
('201', 2, 2, 'Available'),
('202', 2, 2, 'Occupied'),
('301', 3, 3, 'Available'),
('302', 3, 3, 'Under Maintenance');

-- Reservations
INSERT INTO Reservations (guest_id, room_id, staff_id, check_in, check_out, status) VALUES
(1, 2, 1, '2024-06-01', '2024-06-04', 'Checked-Out'),
(2, 4, 2, '2024-06-05', '2024-06-08', 'Checked-Out'),
(3, 5, 1, '2024-07-01', '2024-07-05', 'Checked-In'),
(4, 1, 2, '2024-07-10', '2024-07-12', 'Confirmed'),
(5, 3, 1, '2024-07-15', '2024-07-18', 'Confirmed');

-- Billing (payment info merged here)
INSERT INTO Billing (res_id, room_charge, extra_charge, tax_percent, total, pay_method, pay_status) VALUES
(1,  4500,  500, 18,  5900, 'Cash',        'Paid'),
(2, 10500,  800, 18, 13394, 'UPI',         'Paid'),
(3, 24000,  200, 18, 28556, 'Credit Card', 'Paid'),
(4,  3000,    0, 18,  3540, 'Cash',        'Pending'),
(5, 10500,  300, 18, 12744, 'Net Banking', 'Pending');

-- Housekeeping
INSERT INTO Housekeeping (room_id, staff_id, task_type, task_date, status) VALUES
(2, 3, 'Cleaning',     '2024-06-02', 'Done'),
(4, 3, 'Linen Change', '2024-06-06', 'Done'),
(6, 4, 'Repair',       '2024-06-20', 'Done'),
(5, 3, 'Cleaning',     '2024-07-02', 'Pending'),
(1, 3, 'Inspection',   '2024-07-09', 'Pending');