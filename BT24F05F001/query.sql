-- Non-trivial SQL queries for Student Club Events Database

-- Query 1: Multi-table join - List all registered students for each event with event and club names
SELECT s.name AS student_name, e.name AS event_name, c.name AS club_name
FROM registrations r
JOIN students s ON r.student_id = s.student_id
JOIN events e ON r.event_id = e.event_id
JOIN clubs c ON e.club_id = c.club_id
WHERE r.status = 'registered'
ORDER BY e.name, s.name;


-- Query 2: GROUP BY with HAVING - Find clubs that have organized more than 1 event
SELECT c.name AS club_name, COUNT(e.event_id) AS event_count
FROM clubs c
JOIN events e ON c.club_id = e.club_id
GROUP BY c.club_id, c.name
HAVING COUNT(e.event_id) > 1;


-- Query 3: Subquery - Find events with capacity greater than the average capacity of all events
SELECT name AS event_name, capacity
FROM events
WHERE capacity > (SELECT AVG(capacity) FROM events);


-- Query 4: CREATE VIEW and SELECT from it - Create view for upcoming events and select from it
CREATE VIEW upcoming_events AS
SELECT event_id, name, event_date, capacity, location
FROM events
WHERE event_date >= CURDATE();


SELECT * FROM upcoming_events ORDER BY event_date;


-- Query 5: Business question - How many students are on the waitlist for each event?
SELECT e.name AS event_name, COUNT(r.registration_id) AS waitlist_count
FROM events e
LEFT JOIN registrations r ON e.event_id = r.event_id AND r.status = 'waitlist'
GROUP BY e.event_id, e.name
ORDER BY waitlist_count DESC;


-- Query 6: Find students who are registered for more than 2 events
SELECT s.name AS student_name, COUNT(r.registration_id) AS registration_count
FROM students s
JOIN registrations r ON s.student_id = r.student_id
WHERE r.status = 'registered'
GROUP BY s.student_id, s.name
HAVING COUNT(r.registration_id) > 2;


-- Query 7: List events that are fully booked (registered count equals capacity)
SELECT e.name AS event_name, COUNT(r.registration_id) AS registered_count, e.capacity
FROM events e
JOIN registrations r ON e.event_id = r.event_id AND r.status = 'registered'
GROUP BY e.event_id, e.name, e.capacity
HAVING COUNT(r.registration_id) = e.capacity;


-- Query 8: Find the club with the highest number of events
SELECT c.name AS club_name, COUNT(e.event_id) AS event_count
FROM clubs c
JOIN events e ON c.club_id = e.club_id
GROUP BY c.club_id, c.name
ORDER BY event_count DESC
LIMIT 1;
