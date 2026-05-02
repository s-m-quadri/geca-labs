USE hostel_db;

-- Students (simple roll numbers)
INSERT INTO students (roll_no, name, branch, year, contact_no, address) VALUES
('S101','Alice','Civil',2,'9876543210','Bangalore'),
('S102','Bob','Mech',3,'9876543211','Chennai'),
('S103','Charlie','EEP',4,'9876543212','Kolkata'),
('S104','David','CSE',2,'9876543213','Mumbai'),
('S105','Eve','ENTC',2,'9876543214','Pune'),
('S106','Frank','IT',1,'9876543215','Delhi');

-- Rooms
INSERT INTO rooms (room_no, floor, capacity) VALUES
('101',1,2),
('102',1,2),
('201',2,3),
('202',2,2);

-- Room Allotment
INSERT INTO room_allotment (student_id, room_id, allot_date, vacate_date) VALUES
(1,1,'2026-01-01','2026-12-31'),
(2,2,'2026-01-02','2026-12-31'),
(3,1,'2026-01-03','2026-12-31'),
(4,3,'2026-01-04','2026-12-31'),
(5,3,'2026-01-05','2026-12-31'),
(6,4,'2026-01-06','2026-12-31');

-- Officials
INSERT INTO officials (name, role, contact) VALUES
('Mr.Starc','warden','9991110001'),
('Mr.Johnson','warden','9991110002'),
('Dr.Kumar','rector','8882220001');

-- Complaints
INSERT INTO complaints (student_id, complaint_text, complaint_date, status) VALUES
(1,'Water issue','2026-02-01','pending'),
(2,'Electricity problem','2026-02-02','resolved'),
(3,'WiFi not working','2026-02-03','pending'),
(4,'Cleaning issue','2026-02-04','resolved'),
(5,'Fan not working','2026-02-05','pending'),
(6,'Water leakage','2026-02-06','resolved');