use modern_hotel;

insert into department (name, manager_name) values
('Management', 'George Lucas'),
('Maintenance', 'Steven King');

insert into staff (department_id, full_name, designation, phone_number, salary) values
(1, 'Hannah Abbott', 'Manager', '999-1111', 45000),
(2, 'Ian Malcolm', 'Plumber', '999-2222', 28000);

insert into guest (full_name, email, phone, address, identification) values
('Jack Sparrow', 'jack@sea.com', '999-3333', 'Tortuga', 'ID-777'),
('Kent Clark', 'kent@daily.com', '999-4444', 'Metropolis', 'ID-888');

insert into room_type (title, nightly_rate, max_guests) values
('Standard', 1000, 2),
('Suite', 5000, 4);

insert into room (room_no, type_id, floor_num, state) values
('G-01', 1, 0, 'Free'),
('P-01', 2, 3, 'Occupied');

insert into reservation (guest_id, room_id, staff_id, check_in, check_out, status) values
(2, 2, 1, '2025-01-10', '2025-01-15', 'Active');

insert into billing (reservation_id, room_cost, extras, tax_pct, final_amount, method, status) values
(1, 25000, 0, 18, 29500, 'UPI', 'Paid');