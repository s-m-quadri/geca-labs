SELECT s.name, r.room_number, h.hostel_name
FROM student s
JOIN room r ON s.room_id = r.room_id
JOIN hostel h ON r.hostel_id = h.hostel_id;

SELECT status, COUNT(*) AS total
FROM fee
GROUP BY status;

SELECT h.hostel_name, COUNT(s.student_id) AS students
FROM hostel h
JOIN room r ON h.hostel_id = r.hostel_id
JOIN student s ON r.room_id = s.room_id
GROUP BY h.hostel_name;

SELECT s.name, f.amount
FROM student s
JOIN fee f ON s.student_id = f.student_id
WHERE f.status = 'Pending';

SELECT name
FROM student
WHERE student_id IN (
  SELECT student_id FROM complaint
);

SELECT status, COUNT(*) 
FROM complaint
GROUP BY status;

SELECT h.hostel_name, COUNT(s.student_id) AS total_students
FROM hostel h
JOIN room r ON h.hostel_id = r.hostel_id
JOIN student s ON r.room_id = s.room_id
GROUP BY h.hostel_name
ORDER BY total_students DESC;

SELECT * 
FROM complaint
WHERE status = 'Open';