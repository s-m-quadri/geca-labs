-- Lab 6-v2 -- views & subqueries (PostgreSQL): schema
-- Run: sudo -u postgres psql -f 01_setup.sql

DROP DATABASE IF EXISTS view_lab;
CREATE DATABASE view_lab;
--\c view_lab

CREATE TABLE customers (
  cust_id INT PRIMARY KEY,
  name    VARCHAR(60) NOT NULL
);

CREATE TABLE products (
  prod_id INT PRIMARY KEY,
  name    VARCHAR(60) NOT NULL,
  price   DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
  order_id   INT PRIMARY KEY,
  cust_id    INT NOT NULL,
  order_date DATE NOT NULL,
  FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

CREATE TABLE order_lines (
  order_id INT NOT NULL,
  prod_id  INT NOT NULL,
  qty      INT NOT NULL,
  PRIMARY KEY (order_id, prod_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (prod_id)  REFERENCES products(prod_id)
);

INSERT INTO customers VALUES
  (1, 'Nia'),
  (2, 'Omar'),
  (3, 'Pia'),
  (4, 'Quinn');

INSERT INTO products VALUES
  (10, 'Notebook', 12.00),
  (20, 'PenSet',   25.00),
  (30, 'DeskMat',  25.00),
  (40, 'Lamp',     40.00);

INSERT INTO orders VALUES
  (1001, 1, '2024-01-05'),
  (1002, 1, '2024-02-10'),
  (1003, 2, '2024-01-20'),
  (1004, 3, '2024-03-01');

INSERT INTO order_lines VALUES
  (1001, 10, 2),
  (1001, 20, 1),
  (1002, 40, 1),
  (1002, 10, 1),
  (1003, 30, 1),
  (1003, 20, 2),
  (1004, 10, 5);

SELECT 'view_lab ready' AS status;
