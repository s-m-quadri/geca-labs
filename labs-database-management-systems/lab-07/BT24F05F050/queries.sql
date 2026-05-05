SELECT * FROM Customers;

SELECT restaurant_name, item_name, price
FROM Restaurants r
JOIN Menu_Items m
ON r.restaurant_id = m.restaurant_id;

SELECT c.name, o.order_id, o.status
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id;

SELECT SUM(amount) AS Total_Revenue FROM Payments;

SELECT * FROM Orders
WHERE status='Pending';