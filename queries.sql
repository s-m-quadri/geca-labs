use modern_hotel;

-- 1. Get all free rooms
select r.room_no, rt.title, rt.nightly_rate
from room r
join room_type rt on r.type_id = rt.id
where r.state = 'Free';

-- 2. View current guests in the hotel
select g.full_name, r.room_no, res.check_out
from reservation res
join guest g on res.guest_id = g.id
join room r on res.room_id = r.id
where res.status = 'Active';

-- 3. Total income generated
select sum(final_amount) as total_earnings
from billing
where status = 'Paid';