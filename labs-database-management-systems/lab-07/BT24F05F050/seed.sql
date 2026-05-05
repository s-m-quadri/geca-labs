INSERT INTO Customers(name, phone, address)
VALUES
('Sarthak','9876543210','Aurangabad'),
('Rahul','9988776655','Pune');

INSERT INTO Restaurants(restaurant_name, location)
VALUES
('Spice Hub','Aurangabad'),
('Pizza Point','Pune');

INSERT INTO Menu_Items(restaurant_id, item_name, price)
VALUES
(1,'Paneer Tikka',250),
(1,'Veg Biryani',180),
(2,'Margherita Pizza',300);

INSERT INTO Orders(customer_id, order_date, status)
VALUES
(1,'2026-05-02','Delivered'),
(2,'2026-05-02','Pending');

INSERT INTO Order_Details(order_id, item_id, quantity)
VALUES
(1,1,2),
(1,2,1),
(2,3,1);

INSERT INTO Payments(order_id, amount, payment_mode)
VALUES
(1,680,'UPI'),
(2,300,'Cash');