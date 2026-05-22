-- Note 
-- show databases;
-- create database dbname;
-- use dbname;

-- create table t_name(c1 dt, c2 dt...);
-- desc t_name;

-- insert into t_name values(v1,v2...)
-- insert into tname (c1,c2) values(v1,v2);

-- select * from t_name;
-- select coloum_name from t_name;

-- select * from t_name where condition;
-- select * from t_name where c1 or/and c2;

-- Update command - 
-- syntax -- update t_name set col = name where col = val(condition);

use employee_db;
select * from emp_details;

update emp_details set depat = "Developer" where emp_id = 101;
update emp_deatils set dept = "Faculty" where dept = "sales";

-- delete command
-- syntax : delete from t_name where condition;
delete from emp_details where emp_id = 102;
delete from emp_details where dept = "HR"; 

-- distinct clause
select distinct dept from emp_details;
select distinct city from emp_details;

-- order by clause
select * from emp_details order by salary; -- by default ascending
select * from emp_details order by salary desc;

SET SQL_SAFE_UPDATES = 0;

-- limit clause
select * from emp_details limit 5;
select * from emp_details limit 5,5;

--
create database shopping_db;
use shopping_db;

create table products(product_id int primary key, product_name varchar(32), category varchar(32), 
brand varchar(16),price float, quantity int, rating int);

-- insert task
INSERT INTO products VALUES
(101, 'Laptop', 'Electronics', 'Dell', 65000, 12, 5),
(102, 'Smartphone', 'Electronics', 'Samsung', 32000, 20, 4),
(103, 'Headphones', 'Accessories', 'Boat', 2500, 35, 4),
(104, 'Smart Watch', 'Wearable', 'Noise', 4500, 18, 4),
(105, 'Refrigerator', 'Home Appliance', 'LG', 38000, 6, 5),
(106, 'Microwave Oven', 'Home Appliance', 'IFB', 12000, 10, 4),
(107, 'Office Chair', 'Furniture', 'GreenSoul', 8500, 14, 5),
(108, 'Tablet', 'Electronics', 'Lenovo', 22000, 9, 4),
(109, 'Air Conditioner', 'Home Appliance', 'Voltas', 42000, 5, 5),
(110, 'Bluetooth Speaker', 'Accessories', 'JBL', 3500, 25, 4);

INSERT INTO products VALUES
(111, 'Television', 'Electronics', 'Sony', 55000, 7, 5),
(112, 'Washing Machine', 'Electronics', 'Whirlpool', 28000, 8, 4),

(113, 'Rice Bag', 'Grocery', 'India Gate', 1200, 30, 5),
(114, 'Cooking Oil', 'Grocery', 'Fortune', 1800, 22, 4),
(115, 'Biscuits', 'Grocery', 'Parle', 120, 50, 4),

(116, 'T-Shirt', 'Clothing', 'Puma', 999, 40, 4),
(117, 'Jeans', 'Clothing', 'Levis', 2499, 25, 5),
(118, 'Jacket', 'Clothing', 'Nike', 3999, 15, 5);

-- update task
update products set price = 3243 where product_id = 111;
update products set price = price + (price*10)/100 where category = "electrinics";
update products set quantity = 20, rating = 5 where product_id=109;

-- delete task
delete from products where product_id = 105;
delete from products where category="Grocery";
delete from products where quantity = 0;

-- distinct task
select distinct category from products;
select distinct brand from products;
select distinct rating from products;

-- order by task
select * from products order by price;
select * from products order by rating desc;
select * from products order by category,price;

-- 603@thekiranacademy.com