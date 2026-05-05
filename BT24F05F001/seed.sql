-- Seed data for Student Club Events Database

-- Insert clubs
INSERT INTO clubs (name, description, faculty_advisor) VALUES
('Tech Club', 'For technology and programming enthusiasts', 'Dr. Smith'),
('Art Club', 'Promoting creative arts and expression', 'Prof. Johnson'),
('Sports Club', 'Organizing athletic and sports activities', 'Coach Lee');


-- Insert students
INSERT INTO students (name, email, year) VALUES
('Alice Johnson', 'alice.johnson@email.com', 2),
('Bob Smith', 'bob.smith@email.com', 3),
('Charlie Brown', 'charlie.brown@email.com', 1),
('Diana Prince', 'diana.prince@email.com', 4),
('Eve Wilson', 'eve.wilson@email.com', 2),
('Frank Miller', 'frank.miller@email.com', 3),
('Grace Lee', 'grace.lee@email.com', 1),
('Henry Davis', 'henry.davis@email.com', 4),
('Ivy Chen', 'ivy.chen@email.com', 2),
('Jack Taylor', 'jack.taylor@email.com', 3);


-- Insert events
INSERT INTO events (club_id, name, description, event_date, capacity, location) VALUES
(1, 'Coding Workshop', 'Introduction to Python programming', '2026-05-10', 5, 'Room 101'),
(1, 'Hackathon', '24-hour coding competition', '2026-05-15', 10, 'Auditorium'),
(2, 'Painting Session', 'Watercolor painting workshop', '2026-05-12', 3, 'Art Room'),
(2, 'Sculpture Class', 'Clay modeling and sculpture', '2026-05-18', 4, 'Studio'),
(3, 'Basketball Game', 'Intra-club basketball tournament', '2026-05-20', 8, 'Gym');


-- Insert registrations (simulating registration order and status based on capacity)
-- Event 1 (cap 5): students 1-7 register -> 1-5 registered, 6-7 waitlist
INSERT INTO registrations (student_id, event_id, status) VALUES
(1, 1, 'registered'),
(2, 1, 'registered'),
(3, 1, 'registered'),
(4, 1, 'registered'),
(5, 1, 'registered'),
(6, 1, 'waitlist'),
(7, 1, 'waitlist');


-- Event 2 (cap 10): students 1-10 register -> all registered
INSERT INTO registrations (student_id, event_id, status) VALUES
(1, 2, 'registered'),
(2, 2, 'registered'),
(3, 2, 'registered'),
(4, 2, 'registered'),
(5, 2, 'registered'),
(6, 2, 'registered'),
(7, 2, 'registered'),
(8, 2, 'registered'),
(9, 2, 'registered'),
(10, 2, 'registered');


-- Event 3 (cap 3): students 1-4 register -> 1-3 registered, 4 waitlist
INSERT INTO registrations (student_id, event_id, status) VALUES
(1, 3, 'registered'),
(2, 3, 'registered'),
(3, 3, 'registered'),
(4, 3, 'waitlist');


-- Event 4 (cap 4): students 5-9 register -> 5-8 registered, 9 waitlist
INSERT INTO registrations (student_id, event_id, status) VALUES
(5, 4, 'registered'),
(6, 4, 'registered'),
(7, 4, 'registered'),
(8, 4, 'registered'),
(9, 4, 'waitlist');


-- Event 5 (cap 8): students 1-10 register -> 1-8 registered, 9-10 waitlist
INSERT INTO registrations (student_id, event_id, status) VALUES
(1, 5, 'registered'),
(2, 5, 'registered'),
(3, 5, 'registered'),
(4, 5, 'registered'),
(5, 5, 'registered'),
(6, 5, 'registered'),
(7, 5, 'registered'),
(8, 5, 'registered'),
(9, 5, 'waitlist'),
(10, 5, 'waitlist');
