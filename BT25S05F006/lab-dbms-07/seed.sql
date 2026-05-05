INSERT INTO supplier (name, contact) VALUES
('ABC Traders', '9876543210'),
('XYZ Suppliers', '9123456780');

INSERT INTO product (name, price, supplier_id) VALUES
('Laptop', 50000, 1),
('Mouse', 500, 1),
('Keyboard', 1500, 2),
('Monitor', 12000, 2);

INSERT INTO inventory (product_id, quantity) VALUES
(1, 10),
(2, 50),
(3, 30),
(4, 5);

INSERT INTO orders (order_date) VALUES
('2025-01-01'),
('2025-01-02');

INSERT INTO order_details VALUES
(1, 1, 1),
(1, 2, 2),
(2, 4, 1),
(2, 3, 1);