use product_db;
CREATE TABLE Products ( PID INT PRIMARY KEY, Product_Name VARCHAR(50) NOT NULL, Category
VARCHAR(30) NOT NULL, Price DECIMAL(10,2) NOT NULL );
INSERT INTO Products (PID, Product_Name, Category, Price) VALUES (101, 'Laptop', 'Electronics',
60000), (102, 'Mobile', 'Electronics', 25000), (103, 'Headphones', 'Electronics', 3000), (104, 'Printer',
'Electronics', 15000), (105, 'Smart Watch', 'Electronics', 8000),
(106, 'Chair', 'Furniture', 5000), (107, 'Table', 'Furniture', 8000), (108, 'Sofa', 'Furniture', 25000), (109,
'Bed', 'Furniture', 30000), (110, 'Cupboard', 'Furniture', 18000),
(111, 'Shoes', 'Fashion', 2000), (112, 'T-Shirt', 'Fashion', 1000), (113, 'Watch', 'Fashion', 7000), (114,
'Jeans', 'Fashion', 2500), (115, 'Jacket', 'Fashion', 4500),
(116, 'Rice', 'Grocery', 1200), (117, 'Wheat', 'Grocery', 900), (118, 'Sugar', 'Grocery', 600), (119, 'Tea
Powder', 'Grocery', 450), (120, 'Cooking Oil', 'Grocery', 1800);

select * from Products;

-- Task 1
-- Find all products whose price is greater than the average price of all products.
select * from Products where Price > (select avg(Price) from Products);

-- Task 2
-- Find the most expensive product in the Products table.
select Product_Name from Products where Price = (select max(Price) from Products);

-- Task 3
-- Find the cheapest product in the Products table.
select Product_Name from Products where Price = (select min(Price) from Products);

-- Task 4
-- Find all products that belong to the same category as the Laptop.
select * from Products where Category = (select Category from Products where Product_Name="Laptop");

-- Task 5
-- Find all products whose price is greater than the price of the Mobile.
select * from Products where price > (select price from Products where Product_name = "Mobile");

-- Task 6
-- Find all products that belong to categories having at least one product priced above ₹20,000.
select * from Products where Category in (select Category from Products where price > 20000);

-- Task 7
-- Find the second most expensive product in the Products table.
select Product_name from Products where Price = (select max(Price) from Products where Price < (select max(Price) from Products where Price));

-- Task 8 ---------------------------------------------------------------------------
-- Find products whose price is greater than the average price of their own category.
select distinct Product_name from Products where Price > (select avg(Price) from Products group by Category);

-- Task 9
-- Find the cheapest product from each category.
select Product_name, Category from Products where Price in (select min(Price) from products group by Category);

-- Task 10
-- Find products that are not the most expensive product in their category.
select * from Products p1 where Price not in (select max(Price) from Products p2 where p1.Category=p2.Category);

-- Task 11
-- Find products whose price is less than the average price of the Electronics category.
select * from Products where Price < (select avg(Price) from Products where Category="Electronics");

-- Task 12
-- Find all products belonging to the category of the most expensive product.
select * from Products where Category in (select Category from Products where price = (select max(Price) from Products));

-- Task 13
-- Find products whose price is equal to the highest price in their category.
select * from Products where price in (select max(Price) from Products group by Category);

-- Task 14
-- Find categories where the average product price is greater than ₹10,000 and display all products from those categories.
select * from Products where Category = any(select Category from Products group by Category having avg(Price) > 10000);

-- Task 15
-- Find the third most expensive product in the Products table.
select Product_name from Products where Price = (select distinct Price from Products order by Price desc limit 2,1);

-- Task 16
-- Find all products whose price is greater than the minimum price in the Furniture category.
select * from Products where Price > (select min(Price) from Products where Category = "Furniture");

-- Task 17
-- Find products that have a price greater than every product in the Fashion category.
select * from Products where Price > all (select Price from Products where Category = "Fashion");

-- Task 18 
-- Find products whose price is below the average price of their own category.
select * from Products p1 where Price < (select avg(Price) from Products p2 where p1.Category=p2.Category);

-- Task 19
-- Find categories that contain more than one product and display all products from those categories.
select * from Products where Category in (select Category from Products group by Category having count(*)>1);