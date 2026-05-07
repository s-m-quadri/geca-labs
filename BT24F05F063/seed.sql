-- ============================================================================
-- Hotel Management System - Seed Data
-- Database: view_lab
-- Insert sample data for testing and demonstration
-- ============================================================================

USE view_lab;

-- ============================================================================
-- Insert Guest Data
-- ============================================================================
INSERT INTO guests (name, phone, email) VALUES
('John Smith', '5551234567', 'john.smith@email.com'),
('Sarah Johnson', '5559876543', 'sarah.johnson@email.com'),
('Michael Chen', '5552223334', 'michael.chen@email.com'),
('Emily Rodriguez', '5554445556', 'emily.rodriguez@email.com'),
('David Williams', '5557778889', 'david.williams@email.com');

-- ============================================================================
-- Insert Room Data
-- ============================================================================
INSERT INTO rooms (room_type, price, status) VALUES
('single', 99.99, 'available'),
('double', 149.99, 'available'),
('suite', 299.99, 'occupied'),
('double', 149.99, 'available'),
('single', 99.99, 'maintenance'),
('suite', 299.99, 'available');

-- ============================================================================
-- Insert Staff Data
-- ============================================================================
INSERT INTO staff (name, role, salary) VALUES
('Alice Manager', 'Manager', 50000.00),
('Bob Receptionist', 'Receptionist', 28000.00),
('Carol Housekeeper', 'Housekeeper', 25000.00),
('David Maintenance', 'Maintenance', 30000.00),
('Emma Chef', 'Chef', 40000.00);

-- ============================================================================
-- Insert Booking Data
-- ============================================================================
INSERT INTO bookings (guest_id, room_id, check_in, check_out, total_amount) VALUES
(1, 1, '2026-05-05', '2026-05-07', 199.98),
(2, 2, '2026-05-10', '2026-05-12', 299.98),
(3, 4, '2026-05-15', '2026-05-17', 299.98),
(4, 3, '2026-04-28', '2026-05-02', 1199.96),
(5, 6, '2026-05-20', '2026-05-25', 1499.95);
