
USE hotel_corp_db;

INSERT INTO tbl_departments (department_name, head_manager) VALUES
('Front Office', 'Alice Smith'),
('Cleaning', 'Bob Jones');

INSERT INTO tbl_employees (dept_id, full_name, job_title, contact_no, base_salary) VALUES
(1, 'Charlie Brown', 'Receptionist', '555-0101', 34000),
(2, 'Diana Prince', 'Maid', '555-0202', 24000);

INSERT INTO tbl_guests (full_name, email_address, contact_no, home_address, identity_document) VALUES
('Evan Davis', 'evan@mail.com', '555-0303', 'New York', 'DL-998877'),
('Fiona Gallagher', 'fiona@mail.com', '555-0404', 'Chicago', 'PP-112233');

INSERT INTO tbl_room_categories (category_name, rate_per_night, capacity) VALUES
('Basic', 1200, 2),
('Premium', 4000, 2);

INSERT INTO tbl_rooms (room_number, category_id, floor_level, current_status) VALUES
('10A', 1, 1, 'Available'),
('20B', 2, 2, 'Occupied');

INSERT INTO tbl_bookings (guest_id, room_id, emp_id, check_in_date, check_out_date, booking_status) VALUES
(1, 2, 1, '2024-08-01', '2024-08-05', 'Checked-In');

INSERT INTO tbl_invoices (booking_id, room_fees, additional_fees, tax_rate, grand_total, payment_mode, payment_status) VALUES
(1, 16000, 1000, 18, 20060, 'Card', 'Paid');