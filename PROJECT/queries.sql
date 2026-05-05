USE hostel_db;

-- 1. Students with their room details (JOIN)
SELECT s.name, s.branch, r.room_no, r.floor
FROM students s
JOIN room_allotment ra ON s.student_id = ra.student_id
JOIN rooms r ON ra.room_id = r.room_id;

-- 2. Count of students in each room (GROUP BY)
SELECT r.room_no, COUNT(ra.student_id) AS total_students
FROM rooms r
JOIN room_allotment ra ON r.room_id = ra.room_id
GROUP BY r.room_no;

-- 3. Rooms that are over capacity (HAVING)
SELECT r.room_no, COUNT(ra.student_id) AS occupants, r.capacity
FROM rooms r
JOIN room_allotment ra ON r.room_id = ra.room_id
GROUP BY r.room_no, r.capacity
HAVING COUNT(ra.student_id) > r.capacity;

-- 4. List all pending complaints
SELECT s.name, c.complaint_text, c.complaint_date
FROM complaints c
JOIN students s ON c.student_id = s.student_id
WHERE c.status = 'pending';

-- 5. Count complaints per student
SELECT s.name, COUNT(c.complaint_id) AS total_complaints
FROM students s
LEFT JOIN complaints c ON s.student_id = c.student_id
GROUP BY s.name;

-- 6. Students who have raised at least one complaint (SUBQUERY)
SELECT name
FROM students
WHERE student_id IN (
    SELECT DISTINCT student_id FROM complaints
);

-- 7. Create VIEW: complaint summary
CREATE OR REPLACE VIEW complaint_summary AS
SELECT s.name, c.complaint_text, c.status
FROM students s
JOIN complaints c ON s.student_id = c.student_id;

-- Use view
SELECT * FROM complaint_summary;

-- 8. Most occupied room (Business query)
SELECT r.room_no, COUNT(ra.student_id) AS occupancy
FROM rooms r
JOIN room_allotment ra ON r.room_id = ra.room_id
GROUP BY r.room_no
ORDER BY occupancy DESC
LIMIT 1;

-- 9. List officials (warden + rector)
SELECT name, role, contact
FROM officials;
