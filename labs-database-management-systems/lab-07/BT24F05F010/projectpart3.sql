-- Sample data for Hostel Management System

INSERT INTO hostels (hostel_name, address, total_rooms) VALUES
('North Hostel', '123 Campus Lane', 30),
('South Hostel', '456 Academy Road', 25);

INSERT INTO rooms (hostel_id, room_number, capacity, status) VALUES
(1, '101', 1, 'Available'),
(1, '102', 2, 'Occupied'),
(1, '103', 3, 'Available'),
(2, '201', 1, 'Occupied'),
(2, '202', 2, 'Available'),
(2, '203', 3, 'Occupied');

INSERT INTO students (name, email, phone, enrollment_date) VALUES
('Aadarsh Kumar', 'aadarsh@uni.com', '9111111111', '2026-01-15'),
('Sudhanshu Sharma', 'sudhanshu@uni.com', '9111111112', '2026-01-20'),
('Ravi Patel', 'ravi@uni.com', '9111111113', '2026-02-01'),
('Priya Singh', 'priya@uni.com', '9111111114', '2026-02-10'),
('Arjun Das', 'arjun@uni.com', '9111111115', '2026-02-15');

INSERT INTO allocations (room_id, student_id, check_in_date, status) VALUES
(2, 1, '2026-01-20', 'Active'),
(4, 2, '2026-02-01', 'Active'),
(6, 3, '2026-02-10', 'Active');

INSERT INTO bills (student_id, allocation_id, amount, bill_date, status) VALUES
(1, 1, 5000, '2026-05-01', 'Paid'),
(2, 2, 5000, '2026-05-02', 'Pending'),
(3, 3, 5000, '2026-05-03', 'Pending'),
(4, NULL, 2500, '2026-05-04', 'Pending');
(5, 5, 5600.00, 'Paid', '2026-05-05'),
(6, 6, 750.00, 'Paid', '2026-05-06'),
(7, 7, 6000.00, 'Pending', '2026-05-07'),
(8, 8, 1500.00, 'Paid', '2026-05-08'),
(9, 9, 3600.00, 'Pending', '2026-05-12'),
(10, 10, 3500.00, 'Paid', '2026-05-13');
