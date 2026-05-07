USE hotel_db;


-- Insert Hotels
INSERT INTO Hotel (name, location, rating) VALUES
('Sunrise Inn', 'Pune', 4.2),
('Ocean View', 'Goa', 4.7),
('Mountain Stay', 'Manali', 4.5);


-- Insert Rooms
INSERT INTO Room (hotel_id, room_type, price, availability) VALUES
(1, 'Single', 2000.00, 'Available'),
(1, 'Double', 3500.00, 'Booked'),
(2, 'Deluxe', 5000.00, 'Available'),
(2, 'Suite', 8000.00, 'Available'),
(3, 'Standard', 2500.00, 'Booked');


-- Insert Guests
INSERT INTO Guest (name, phone, email, address) VALUES
('Amit Sharma', '9000000001', 'amit@gmail.com', 'Pune'),
('Neha Kapoor', '9000000002', 'neha@gmail.com', 'Mumbai'),
('Rahul Verma', '9000000003', 'rahul@gmail.com', 'Delhi');


-- Insert Bookings
INSERT INTO Booking (guest_id, room_id, check_in, check_out, status) VALUES
(1, 2, '2026-05-01', '2026-05-03', 'Completed'),
(2, 3, '2026-05-02', '2026-05-05', 'Confirmed'),
(3, 5, '2026-05-03', '2026-05-06', 'Cancelled'),
(1, 1, '2026-05-10', '2026-05-12', 'Confirmed');


-- Insert Payments
INSERT INTO Payment (booking_id, amount, payment_date, paid) VALUES
(1, 7000.00, '2026-05-01', 'Yes'),
(2, 15000.00, '2026-05-02', 'No'),
(3, 8000.00, '2026-05-03', 'No'),
(4, 4000.00, '2026-05-10', 'Yes');