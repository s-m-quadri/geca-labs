-- queries.sql: Useful Queries for Student Attendance System
-- ------------------------------------------------------

-- 1. Get attendance of a specific student (by student_id)
SELECT a.date, c.class_name, a.status
FROM Attendance a
JOIN Classes c ON a.class_id = c.class_id
WHERE a.student_id = 1
ORDER BY a.date, c.class_name;

-- 2. Get attendance percentage per student
SELECT s.student_id, s.name,
  ROUND(100 * SUM(a.status = 'Present') / COUNT(*), 2) AS attendance_percentage
FROM Students s
JOIN Attendance a ON s.student_id = a.student_id
GROUP BY s.student_id, s.name;

-- 3. List students with low attendance (<75%)
SELECT s.student_id, s.name,
  ROUND(100 * SUM(a.status = 'Present') / COUNT(*), 2) AS attendance_percentage
FROM Students s
JOIN Attendance a ON s.student_id = a.student_id
GROUP BY s.student_id, s.name
HAVING attendance_percentage < 75;

-- 4. Get class-wise attendance report
SELECT c.class_id, c.class_name, a.date,
  SUM(a.status = 'Present') AS present_count,
  SUM(a.status = 'Absent') AS absent_count
FROM Attendance a
JOIN Classes c ON a.class_id = c.class_id
GROUP BY c.class_id, c.class_name, a.date
ORDER BY c.class_id, a.date;

-- 5. Count present/absent per class
SELECT c.class_name, a.status, COUNT(*) AS count
FROM Attendance a
JOIN Classes c ON a.class_id = c.class_id
GROUP BY c.class_name, a.status;

-- 6. Join query: students + classes + teachers
SELECT s.name AS student, c.class_name, t.name AS teacher
FROM Students s
JOIN Attendance a ON s.student_id = a.student_id
JOIN Classes c ON a.class_id = c.class_id
JOIN Teachers t ON c.teacher_id = t.teacher_id
ORDER BY s.name, c.class_name;

-- 7. Date-wise attendance tracking
SELECT a.date, s.name AS student, c.class_name, a.status
FROM Attendance a
JOIN Students s ON a.student_id = s.student_id
JOIN Classes c ON a.class_id = c.class_id
ORDER BY a.date, s.name;

-- BONUS: Attendance Summary VIEW
CREATE OR REPLACE VIEW AttendanceSummary AS
SELECT s.student_id, s.name, c.class_name,
  COUNT(*) AS total_classes,
  SUM(a.status = 'Present') AS total_present,
  SUM(a.status = 'Absent') AS total_absent,
  ROUND(100 * SUM(a.status = 'Present') / COUNT(*), 2) AS attendance_percentage
FROM Attendance a
JOIN Students s ON a.student_id = s.student_id
JOIN Classes c ON a.class_id = c.class_id
GROUP BY s.student_id, s.name, c.class_name;

-- BONUS: Stored Procedure to mark attendance
DELIMITER //
CREATE PROCEDURE MarkAttendance(
    IN p_student_id INT,
    IN p_class_id INT,
    IN p_date DATE,
    IN p_status ENUM('Present', 'Absent')
)
BEGIN
    INSERT INTO Attendance (student_id, class_id, date, status)
    VALUES (p_student_id, p_class_id, p_date, p_status);
END //
DELIMITER ;

-- BONUS: Trigger to prevent duplicate attendance entry per day
DELIMITER //
CREATE TRIGGER PreventDuplicateAttendance
BEFORE INSERT ON Attendance
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT 1 FROM Attendance
        WHERE student_id = NEW.student_id
          AND class_id = NEW.class_id
          AND date = NEW.date
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Duplicate attendance entry for this student, class, and date.';
    END IF;
END //
DELIMITER ;
