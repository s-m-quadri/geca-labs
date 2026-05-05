# Smart Inventory System - Schema

## About the Tables

In this project, I have created 5 main tables:

1. **Supplier**
   - This table stores information about suppliers.
   - Columns: supplier_id (Primary Key), name, contact

2. **Product**
   - This table stores product details.
   - Columns: product_id (Primary Key), name, price, supplier_id (Foreign Key)

3. **Inventory**
   - This table keeps track of how many items are available in stock.
   - Columns: inventory_id (Primary Key), product_id (Foreign Key), quantity

4. **Orders**
   - This table stores order information.
   - Columns: order_id (Primary Key), order_date

5. **Order_Details**
   - This table connects orders and products.
   - Columns: order_id, product_id, quantity
   - Primary Key: (order_id, product_id)

---

##  Relationships

- One supplier can supply many products (1:N)
- Each product belongs to only one supplier
- Each product has one inventory record (1:1)
- One order can have multiple products
- One product can be in multiple orders

So, there is a many-to-many relationship between Orders and Products, which is handled using the Order_Details table.

---

##  My Design Thinking

- I used primary keys to uniquely identify each record
- I used foreign keys to connect tables properly
- I created a separate inventory table to manage stock easily
- I used a junction table (Order_Details) to handle many-to-many relationships
- I tried to keep the database normalized to avoid data duplication

---

##  Summary

- Supplier → Product : One to Many  
- Product → Inventory : One to One  
- Orders ↔ Products : Many to Many