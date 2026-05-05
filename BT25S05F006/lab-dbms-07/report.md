# Smart Inventory System - Report

##  Problem

In many small shops or businesses, inventory is managed manually.  
This can cause problems like not knowing how much stock is left or which products are selling more.

---

##  Solution

To solve this problem, I created a Smart Inventory System using a database.

This system helps to:
- Keep track of products
- Manage stock levels
- Store order details
- Identify low stock items
- Analyze sales

---

##  Design

I created 5 tables:
- Supplier
- Product
- Inventory
- Orders
- Order_Details

I used foreign keys to connect tables and maintain relationships.  
I also used a junction table to handle many-to-many relationships between orders and products.

The database is normalized, so there is no unnecessary data duplication.

---

##  What My Queries Do

I wrote different SQL queries to:
- Join multiple tables and display data
- Calculate total sales
- Find low stock products
- Calculate total revenue
- Find top-selling product

These queries help in understanding business data better.

---

##  Features

- Joins between tables
- Aggregate functions like SUM and AVG
- GROUP BY and HAVING
- Subqueries
- View creation

---

##  Limitations

- No login system
- No user interface
- Data is limited for testing
- Not connected to real-time system

---

##  Future Improvements

- Add login and authentication
- Create a web or mobile app
- Add automatic low stock alerts
- Improve UI for better usability

---

## Conclusion

This project helped me understand how databases work in real-life applications.  
It shows how inventory can be managed efficiently using SQL and proper database design.