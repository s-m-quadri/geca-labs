-- Queries File

USE hotel_db;

-- 1. Show all rooms with type and price
SELECT r.room_no, rt.type_name, rt.price_per_night, r.floor, r.status
FROM Rooms r
JOIN RoomTypes rt ON r.type_id = rt.type_id;

-- 2. Show all available rooms
SELECT r.room_no, rt.type_name, rt.price_per_night
FROM Rooms r
JOIN RoomTypes rt ON r.type_id = rt.type_id
WHERE r.status = 'Available';

-- 3. Show all guests
SELECT * FROM Guests;

-- 4. Show all active reservations
SELECT r.res_id, g.name AS guest_name, rm.room_no,
       r.check_in, r.check_out, r.status
FROM Reservations r
JOIN Guests g  ON r.guest_id = g.guest_id
JOIN Rooms  rm ON r.room_id  = rm.room_id
WHERE r.status != 'Cancelled';

-- 5. Guests currently checked in
SELECT g.name, g.phone, rm.room_no, r.check_in, r.check_out
FROM Reservations r
JOIN Guests g  ON r.guest_id = g.guest_id
JOIN Rooms  rm ON r.room_id  = rm.room_id
WHERE r.status = 'Checked-In';

-- 6. Total revenue collected (paid bills only)
SELECT SUM(total) AS total_revenue
FROM Billing
WHERE pay_status = 'Paid';

-- 7. Number of bookings per room type
SELECT rt.type_name, COUNT(r.res_id) AS total_bookings
FROM Reservations r
JOIN Rooms     rm ON r.room_id  = rm.room_id
JOIN RoomTypes rt ON rm.type_id = rt.type_id
GROUP BY rt.type_name;

-- 8. Room occupancy summary
SELECT status, COUNT(*) AS count
FROM Rooms
GROUP BY status;

-- 9. Pending housekeeping tasks
SELECT h.task_id, rm.room_no, h.task_type, s.name AS assigned_to, h.task_date
FROM Housekeeping h
JOIN Rooms rm ON h.room_id  = rm.room_id
JOIN Staff s  ON h.staff_id = s.staff_id
WHERE h.status = 'Pending';

-- 10. Full bill details per reservation
SELECT r.res_id, g.name AS guest, rm.room_no,
       b.room_charge, b.extra_charge, b.tax_percent, b.total,
       b.pay_method, b.pay_status
FROM Reservations r
JOIN Guests  g  ON r.guest_id = g.guest_id
JOIN Rooms   rm ON r.room_id  = rm.room_id
JOIN Billing b  ON b.res_id   = r.res_id;

-- 11. Average bill per room type
SELECT rt.type_name, ROUND(AVG(b.total), 2) AS avg_bill
FROM Billing b
JOIN Reservations r  ON b.res_id   = r.res_id
JOIN Rooms        rm ON r.room_id  = rm.room_id
JOIN RoomTypes    rt ON rm.type_id = rt.type_id
GROUP BY rt.type_name;

-- 12. Staff count and salary per department
SELECT d.dept_name, COUNT(s.staff_id) AS staff_count, SUM(s.salary) AS total_salary
FROM Departments d
LEFT JOIN Staff s ON d.dept_id = s.dept_id
GROUP BY d.dept_name;

-- 13. Rooms that have never been booked
SELECT room_no, status
FROM Rooms
WHERE room_id NOT IN (SELECT DISTINCT room_id FROM Reservations);

-- 14. Guest with highest total spending
SELECT g.name, SUM(b.total) AS total_spent
FROM Guests g
JOIN Reservations r ON g.guest_id = r.guest_id
JOIN Billing      b ON r.res_id   = b.res_id
GROUP BY g.guest_id
ORDER BY total_spent DESC
LIMIT 1;

-- 15. Check-in a guest (transaction)
START TRANSACTION;
UPDATE Reservations SET status = 'Checked-In' WHERE res_id = 4;
UPDATE Rooms SET status = 'Occupied'
  WHERE room_id = (SELECT room_id FROM Reservations WHERE res_id = 4);
COMMIT;

-- 16. Check-out a guest (transaction)
START TRANSACTION;
UPDATE Reservations SET status = 'Checked-Out' WHERE res_id = 3;
UPDATE Rooms SET status = 'Available'
  WHERE room_id = (SELECT room_id FROM Reservations WHERE res_id = 3);
COMMIT;

-- 17. View: room occupancy at a glance
CREATE OR REPLACE VIEW vw_room_status AS
SELECT r.room_no, rt.type_name, r.status,
       g.name AS guest_name, res.check_in, res.check_out
FROM Rooms r
JOIN RoomTypes rt ON r.type_id = rt.type_id
LEFT JOIN Reservations res ON res.room_id = r.room_id AND res.status = 'Checked-In'
LEFT JOIN Guests       g   ON res.guest_id = g.guest_id;

SELECT * FROM vw_room_status;