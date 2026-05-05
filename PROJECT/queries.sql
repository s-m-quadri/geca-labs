-- ============================================================================
-- Hotel Management System - SQL Queries
-- Database: view_lab
-- Various queries demonstrating joins, aggregations, grouping, and filtering
-- ============================================================================

USE view_lab;

-- ============================================================================
-- Query 1: JOIN - Guest Booking Details
-- Display all bookings with guest names and room information
-- ============================================================================
SELECT 
    b.booking_id,
    g.name AS guest_name,
    g.email,
    r.room_type,
    r.price,
    b.check_in,
    b.check_out,
    b.total_amount
FROM bookings b
JOIN guests g ON b.guest_id = g.guest_id
JOIN rooms r ON b.room_id = r.room_id
ORDER BY b.check_in DESC;

-- ============================================================================
-- Query 2: AGGREGATION - Total Revenue
-- Calculate total revenue from all bookings
-- ============================================================================
SELECT 
    COUNT(booking_id) AS total_bookings,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS average_booking_value,
    MIN(total_amount) AS lowest_booking,
    MAX(total_amount) AS highest_booking
FROM bookings;

-- ============================================================================
-- Query 3: GROUP BY - Bookings Per Guest
-- Show number of bookings and total spending per guest
-- ============================================================================
SELECT 
    g.guest_id,
    g.name,
    g.email,
    COUNT(b.booking_id) AS number_of_bookings,
    SUM(b.total_amount) AS total_spent,
    AVG(b.total_amount) AS average_booking_amount
FROM guests g
LEFT JOIN bookings b ON g.guest_id = b.guest_id
GROUP BY g.guest_id, g.name, g.email
ORDER BY total_spent DESC;

-- ============================================================================
-- Query 4: SUBQUERY - Highest Priced Room
-- Find bookings for the most expensive room type
-- ============================================================================
SELECT 
    b.booking_id,
    g.name AS guest_name,
    r.room_type,
    r.price,
    b.check_in,
    b.check_out,
    b.total_amount
FROM bookings b
JOIN guests g ON b.guest_id = g.guest_id
JOIN rooms r ON b.room_id = r.room_id
WHERE r.room_id = (
    SELECT room_id FROM rooms ORDER BY price DESC LIMIT 1
);

-- ============================================================================
-- Query 5: FILTERING - Available Rooms
-- List all rooms currently available for booking
-- ============================================================================
SELECT 
    room_id,
    room_type,
    price,
    status
FROM rooms
WHERE status = 'available'
ORDER BY price ASC;

-- ============================================================================
-- Query 6: FILTERING - Ongoing Bookings
-- Show all current and future bookings as of May 2, 2026
-- ============================================================================
SELECT 
    b.booking_id,
    g.name AS guest_name,
    r.room_type,
    b.check_in,
    b.check_out,
    DATEDIFF(b.check_out, b.check_in) AS nights,
    b.total_amount
FROM bookings b
JOIN guests g ON b.guest_id = g.guest_id
JOIN rooms r ON b.room_id = r.room_id
WHERE b.check_in >= CURDATE() OR b.check_out >= CURDATE()
ORDER BY b.check_in ASC;

-- ============================================================================
-- Query 7: Room Type Revenue Analysis
-- Aggregate revenue by room type
-- ============================================================================
SELECT 
    r.room_type,
    COUNT(b.booking_id) AS bookings_count,
    SUM(b.total_amount) AS total_revenue,
    AVG(r.price) AS average_room_price,
    MAX(r.price) AS max_room_price
FROM rooms r
LEFT JOIN bookings b ON r.room_id = b.room_id
GROUP BY r.room_type
ORDER BY total_revenue DESC;

-- ============================================================================
-- Query 8: Guest History with Count
-- Show guests with number of previous bookings
-- ============================================================================
SELECT 
    g.guest_id,
    g.name,
    g.phone,
    g.email,
    COUNT(b.booking_id) AS booking_history
FROM guests g
LEFT JOIN bookings b ON g.guest_id = b.guest_id
GROUP BY g.guest_id, g.name, g.phone, g.email
HAVING COUNT(b.booking_id) > 0
ORDER BY booking_history DESC;

-- ============================================================================
-- Query 9: Rooms Needing Maintenance
-- Find rooms with maintenance status
-- ============================================================================
SELECT 
    room_id,
    room_type,
    price,
    status
FROM rooms
WHERE status = 'maintenance';

-- ============================================================================
-- Query 10: Staff Salary Distribution
-- Show staffing details and salary information
-- ============================================================================
SELECT 
    staff_id,
    name,
    role,
    salary,
    (SELECT COUNT(*) FROM staff) AS total_staff,
    (SELECT AVG(salary) FROM staff) AS average_salary,
    ROUND((salary / (SELECT AVG(salary) FROM staff)) * 100, 2) AS salary_percentage_of_avg
FROM staff
ORDER BY salary DESC;
