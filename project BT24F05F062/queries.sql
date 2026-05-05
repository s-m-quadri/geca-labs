USE hotel_db;


-- Query 1: List all guests
SELECT * FROM Guest;


-- Query 2: List all rooms with hotel names
SELECT 
    r.room_id,
    h.name AS hotel_name,
    r.room_type,
    r.price
FROM Room r
JOIN Hotel h ON r.hotel_id = h.hotel_id;


-- Query 3: View all bookings with guest and room info
SELECT 
    b.booking_id,
    g.name AS guest_name,
    r.room_type,
    b.check_in,
    b.check_out,
    b.status
FROM Booking b
JOIN Guest g ON b.guest_id = g.guest_id
JOIN Room r ON b.room_id = r.room_id;


-- Query 4: Show unpaid payments
SELECT 
    p.payment_id,
    g.name AS guest_name,
    p.amount
FROM Payment p
JOIN Booking b ON p.booking_id = b.booking_id
JOIN Guest g ON b.guest_id = g.guest_id
WHERE p.paid = 'No';


-- Query 5: Total bookings per hotel
SELECT 
    h.name AS hotel_name,
    COUNT(b.booking_id) AS total_bookings
FROM Booking b
JOIN Room r ON b.room_id = r.room_id
JOIN Hotel h ON r.hotel_id = h.hotel_id
GROUP BY h.hotel_id, h.name;


-- Query 6: Bookings of a specific guest (Amit Sharma)
SELECT 
    b.check_in,
    b.check_out,
    r.room_type,
    b.status
FROM Booking b
JOIN Room r ON b.room_id = r.room_id
WHERE b.guest_id = 1;


-- Query 7: Total revenue (paid only)
SELECT 
    SUM(amount) AS total_revenue
FROM Payment
WHERE paid = 'Yes';


-- Query 8: Rooms booked at least 2 times
SELECT 
    r.room_type,
    COUNT(b.booking_id) AS total_bookings
FROM Booking b
JOIN Room r ON b.room_id = r.room_id
GROUP BY r.room_id, r.room_type
HAVING COUNT(b.booking_id) >= 2;


-- Query 9: Upcoming bookings
SELECT 
    g.name AS guest_name,
    r.room_type,
    b.check_in
FROM Booking b
JOIN Guest g ON b.guest_id = g.guest_id
JOIN Room r ON b.room_id = r.room_id
WHERE b.status = 'Confirmed';


-- Query 10: Payment summary per guest
SELECT 
    g.name AS guest_name,
    COUNT(p.payment_id) AS total_payments,
    SUM(p.amount) AS total_amount,
    SUM(CASE WHEN p.paid = 'Yes' THEN p.amount ELSE 0 END) AS amount_paid
FROM Payment p
JOIN Booking b ON p.booking_id = b.booking_id
JOIN Guest g ON b.guest_id = g.guest_id
GROUP BY g.guest_id, g.name;