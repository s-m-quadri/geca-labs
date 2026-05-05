INSERT INTO Passenger (name, email, phone) VALUES
('Amit', 'amit@gmail.com', '9876543210'),
('Riya', 'riya@gmail.com', '9876543211'),
('Rahul', 'rahul@gmail.com', '9876543212'),
('Sneha', 'sneha@gmail.com', '9876543213'),
('Vikram', 'vikram@gmail.com', '9876543214'),
('Pooja', 'pooja@gmail.com', '9876543215'),
('Karan', 'karan@gmail.com', '9876543216'),
('Neha', 'neha@gmail.com', '9876543217');

INSERT INTO Vehicle (type, name, total_seats) VALUES
('Train', 'Deccan Express', 100),
('Bus', 'MSRTC Volvo', 40);

INSERT INTO Route (source, destination, distance_km) VALUES
('Mumbai', 'Pune', 150),
('Aurangabad', 'Pune', 230),
('Mumbai', 'Nashik', 170);

INSERT INTO Trip (vehicle_id, route_id, travel_date, departure_time) VALUES
(1,1,'2026-05-05','08:00'),
(2,2,'2026-05-05','10:00'),
(1,3,'2026-05-06','09:00'),
(2,1,'2026-05-06','11:00'),
(1,2,'2026-05-07','07:00'),
(2,3,'2026-05-07','12:00'),
(1,1,'2026-05-08','08:30'),
(2,2,'2026-05-08','10:30');

INSERT INTO Seat (vehicle_id, seat_number) VALUES
(1,'A1'),(1,'A2'),(1,'A3'),(1,'A4'),
(2,'B1'),(2,'B2'),(2,'B3'),(2,'B4');

INSERT INTO Booking (passenger_id, trip_id, seat_id, booking_date, status) VALUES
(1,1,1,'2026-05-01','Booked'),
(2,1,2,'2026-05-01','Booked'),
(3,2,5,'2026-05-02','Booked'),
(4,3,3,'2026-05-02','Cancelled'),
(5,4,6,'2026-05-03','Booked'),
(6,5,4,'2026-05-03','Booked'),
(7,6,7,'2026-05-04','Booked'),
(8,7,8,'2026-05-04','Booked');