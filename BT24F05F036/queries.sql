-- Passenger booking details with route
SELECT p.name, r.source, r.destination, b.status
FROM Passenger p
JOIN Booking b ON p.passenger_id = b.passenger_id
JOIN Trip t ON b.trip_id = t.trip_id
JOIN Route r ON t.route_id = r.route_id;

-- Passengers with more than 1 booking
SELECT p.name, COUNT(*) AS total_bookings
FROM Passenger p
JOIN Booking b ON p.passenger_id = b.passenger_id
GROUP BY p.name
HAVING COUNT(*) > 1;

-- Trips with no bookings
SELECT trip_id
FROM Trip
WHERE trip_id NOT IN (SELECT trip_id FROM Booking);

-- Which route is most popular?
SELECT r.source, r.destination, COUNT(*) AS bookings
FROM Route r
JOIN Trip t ON r.route_id = t.route_id
JOIN Booking b ON t.trip_id = b.trip_id
GROUP BY r.source, r.destination
ORDER BY bookings DESC;

-- Bookings per trip
SELECT trip_id, COUNT(*) 
FROM Booking
GROUP BY trip_id;

CREATE VIEW ActiveBookings AS
SELECT p.name, t.trip_id, b.status
FROM Passenger p
JOIN Booking b ON p.passenger_id = b.passenger_id
JOIN Trip t ON b.trip_id = t.trip_id;

SELECT * FROM ActiveBookings;

-- Upcoming trips
SELECT *
FROM Trip
WHERE travel_date >= CURRENT_DATE;

-- Prevent double booking of same seat in same trip
CREATE OR REPLACE FUNCTION prevent_double_booking()
RETURNS TRIGGER AS $$
BEGIN
IF EXISTS (
    SELECT 1 FROM Booking
    WHERE trip_id = NEW.trip_id
    AND seat_id = NEW.seat_id
) THEN
    RAISE EXCEPTION 'Seat already booked for this trip';
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER seat_booking_check
BEFORE INSERT ON Booking
FOR EACH ROW
EXECUTE FUNCTION prevent_double_booking();