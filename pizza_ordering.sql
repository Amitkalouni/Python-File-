-- Create database
CREATE DATABASE IF NOT EXISTS pizza_ordering;

-- Use database
USE pizza_ordering;

-- Create table for menu
CREATE TABLE IF NOT EXISTS pizza_menu (
    pizza_id INT AUTO_INCREMENT PRIMARY KEY,
    pizza_name VARCHAR(100),
    size VARCHAR(10),
    price DECIMAL(5,2)
);

-- Create table for orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for order details
CREATE TABLE IF NOT EXISTS order_details (
    detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    pizza_id INT,
    quantity INT,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(pizza_id) REFERENCES pizza_menu(pizza_id)
);

-- Insert some pizzas into menu
INSERT INTO pizza_menu (pizza_name, size, price) VALUES
('Margherita', 'Small', 499.99),
('Margherita', 'Medium', 749.99),
('Margherita', 'Large', 945.99),
('Pepperoni', 'Small', 649.99),
('Pepperoni', 'Medium', 879.99),
('Pepperoni', 'Large', 100.99),
('Veggie', 'Small', 500.49),
('Veggie', 'Medium', 700.49),
('Veggie', 'Large', 900.49);

SELECT o.order_id, o.customer_name, o.order_date, 
       pm.pizza_name, pm.size, od.quantity, 
       (pm.price * od.quantity) AS total_price
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN pizza_menu pm ON od.pizza_id = pm.pizza_id
ORDER BY o.order_id;



select * from pizza_menu;

select * from order_details;

select * from orders;

 
