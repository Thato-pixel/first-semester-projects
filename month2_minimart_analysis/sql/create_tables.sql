CREATE TABLE customer (
customer_id SERIAL PRIMARY KEY,
name VARCHAR(100),
email VARCHAR (100) UNIQUE,
join_date DATE

);


CREATE TABLE products (
product_id SERIAL PRIMARY KEY,
product_name VARCHAR (100),
category VARCHAR(50),
price DECIMAL(10,2)

);

CREATE TABLE orders (
order_id SERIAL PRIMARY KEY,
customer_id INT REFERENCES customer(customer_id),
product_id INT REFERENCES products (product_id),
quantity INT,
order_date DATE

);


