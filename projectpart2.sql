-- HOSTEL MANAGEMENT SYSTEM - PROCEDURES & QUERIES

-- PROCEDURE 1: Allocate room to student
DELIMITER $$
CREATE PROCEDURE allocate_room(IN p_student_id INT, IN p_room_id INT)
BEGIN
  INSERT INTO allocations (room_id, student_id, check_in_date, status)
  VALUES (p_room_id, p_student_id, CURDATE(), 'Active');
  UPDATE rooms SET status = 'Occupied' WHERE room_id = p_room_id;
END $$
DELIMITER ;

-- PROCEDURE 2: Check-out student
DELIMITER $$
CREATE PROCEDURE checkout_student(IN p_allocation_id INT)
BEGIN
  UPDATE allocations SET check_out_date = CURDATE(), status = 'Completed'
  WHERE allocation_id = p_allocation_id;
  UPDATE rooms SET status = 'Available' WHERE room_id =
    (SELECT room_id FROM allocations WHERE allocation_id = p_allocation_id);
END $$
DELIMITER ;

-- PROCEDURE 3: Generate monthly bill
DELIMITER $$
CREATE PROCEDURE generate_bill(IN p_student_id INT, IN p_amount DECIMAL(10,2))
BEGIN
  INSERT INTO bills (student_id, amount, bill_date, status)
  VALUES (p_student_id, p_amount, CURDATE(), 'Pending');
END $$
DELIMITER ;

-- PROCEDURE 4: Pay bill
DELIMITER $$
CREATE PROCEDURE pay_bill(IN p_bill_id INT)
BEGIN
  UPDATE bills SET status = 'Paid' WHERE bill_id = p_bill_id;
END $$
DELIMITER ;

-- QUERY 1: Active allocations with student names
SELECT s.name, r.room_number, a.check_in_date, h.hostel_name
FROM allocations a
JOIN students s ON a.student_id = s.student_id
JOIN rooms r ON a.room_id = r.room_id
JOIN hostels h ON r.hostel_id = h.hostel_id
WHERE a.status = 'Active';

-- QUERY 2: Pending bills (GROUP BY with aggregates)
SELECT s.name, COUNT(b.bill_id) AS pending_count, SUM(b.amount) AS total_pending
FROM bills b
JOIN students s ON b.student_id = s.student_id
WHERE b.status = 'Pending'
GROUP BY b.student_id, s.name;

-- QUERY 3: Room occupancy by hostel (JOIN with GROUP BY)
SELECT h.hostel_name, r.room_number, COUNT(a.allocation_id) AS occupied
FROM rooms r
JOIN hostels h ON r.hostel_id = h.hostel_id
LEFT JOIN allocations a ON r.room_id = a.room_id AND a.status = 'Active'
GROUP BY r.room_id;

-- QUERY 4: Revenue summary by hostel (Subquery with aggregates)
SELECT h.hostel_name, SUM(b.amount) AS paid_amount
FROM bills b
JOIN allocations a ON b.allocation_id = a.allocation_id
JOIN rooms r ON a.room_id = r.room_id
JOIN hostels h ON r.hostel_id = h.hostel_id
WHERE b.status = 'Paid'
GROUP BY h.hostel_id;
