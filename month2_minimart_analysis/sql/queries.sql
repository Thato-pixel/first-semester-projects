-- SQL queries for retrieving insights
 Queries
SELECT * FROM customer;
SELECT * FROM products;
SELECT * FROM products WHERE category = 'Drinks';
SELECT * FROM orders ORDER BY order_date DESC;

Aggregation
SELECT COUNT(order_id) AS TotalOrders FROM orders;
SELECT AVG(price) AS AverageProductPrice FROM products;
SELECT SUM(P.price * O.quantity) AS TotalRevenue FROM orders O JOIN products P ON O.product_id = P.product_id;

Joins
SELECT O.order_id, C.name AS CustomerName, P.product_name, O.quantity FROM orders O INNER JOIN customer C ON O.customer_id = C.customer_id INNER JOIN products P ON O.product_id = P.product_id;
SELECT C.name AS CustomerName, O.order_id, O.order_date FROM customer C LEFT JOIN orders O ON C.customer_id = O.customer_id;
SELECT P.product_name, O.order_id FROM products P LEFT JOIN orders O ON P.product_id = O.product_id WHERE O.order_id IS NULL;
