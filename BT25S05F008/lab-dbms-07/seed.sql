INSERT INTO center (name, location) VALUES
('City Hospital', 'Aurangabad'),
('Bank of India', 'Aurangabad');

INSERT INTO service (center_id, service_name) VALUES
(1, 'General Checkup'),
(1, 'Blood Test'),
(2, 'Account Opening'),
(2, 'Cash Deposit');

INSERT INTO user_table (name, phone) VALUES
('Vedika', '9876543210'),
('Amit', '9123456780'),
('Neha', '9988776655'),
('Ravi', '9871234567');

INSERT INTO token (user_id, service_id, token_number, status) VALUES
(1,1,101,'waiting'),
(2,1,102,'serving'),
(3,2,201,'waiting'),
(4,3,301,'completed'),
(1,4,302,'waiting'),
(2,2,202,'completed'),
(3,3,303,'waiting'),
(4,1,103,'waiting');