DROP DATABASE IF EXISTS smart_inventory;
CREATE DATABASE smart_inventory;
\c smart_inventory;

-- Suppliers
CREATE TABLE supplier (
  supplier_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  contact VARCHAR(15)
);

-- Products
CREATE TABLE product (
  product_id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  supplier_id INT REFERENCES supplier(supplier_id)
);

-- Inventory (stock tracking)
CREATE TABLE inventory (
  inventory_id SERIAL PRIMARY KEY,
  product_id INT REFERENCES product(product_id),
  quantity INT NOT NULL
);

-- Orders (sales)
CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  order_date DATE NOT NULL
);

-- Order Details (junction table)
CREATE TABLE order_details (
  order_id INT REFERENCES orders(order_id),
  product_id INT REFERENCES product(product_id),
  quantity INT,
  PRIMARY KEY (order_id, product_id)
);