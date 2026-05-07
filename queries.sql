USE hotel_corp_db;

-- 1. Display all available accommodations
SELECT rm.room_number, cat.category_name, cat.rate_per_night
FROM tbl_rooms rm
INNER JOIN tbl_room_categories cat ON rm.category_id = cat.category_id
WHERE rm.current_status = 'Available';

-- 2. View active bookings
SELECT bk.booking_id, g.full_name, rm.room_number, bk.check_in_date
FROM tbl_bookings bk
INNER JOIN tbl_guests g ON bk.guest_id = g.guest_id
INNER JOIN tbl_rooms rm ON bk.room_id = rm.room_id
WHERE bk.booking_status = 'Checked-In';

-- 3. Calculate total department salaries
SELECT dept.department_name, SUM(emp.base_salary) AS total_payroll
FROM tbl_departments dept
LEFT JOIN tbl_employees emp ON dept.id = emp.dept_id
GROUP BY dept.department_name;