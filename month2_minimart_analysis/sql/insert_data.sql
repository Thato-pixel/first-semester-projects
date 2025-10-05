-- SQL script to insert sample data
INSERT INTO customer (name, email, join_date) VALUES
('thato matlali', 'thato@example.com', '2023-01-15'),
('Bopane chaole', 'bopane@example.com', '2023-02-10'),
('eche okolo', 'eche@example.com', '2023-03-05'),
('cyril addai', 'addai@example.com', '2023-04-12'),
('lineo matlali', 'lineo@example.com', '2023-05-20');

INSERT INTO products (product_name, category, price) VALUES
('Coca-Cola', 'Drinks', 1.50),
('Pepsi', 'Drinks', 1.40),
('Bread', 'Food', 2.00),
('Laptop', 'Electronics', 800.00),
('Headphones', 'Electronics', 50.00);

INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 3, '2023-06-01'),
(2, 3, 2, '2023-06-03'),
(3, 4, 1, '2023-06-05'),
(1, 5, 1, '2023-06-06'),
(4, 2, 5, '2023-06-07');