# Delete column
alter table courses drop column course;

# modify column
alter table courses modify fee int;

# change column name
alter table courses change fee course_fee float;

# rename table name
alter table courses rename to course_details;

# Task
create database product_db;
use product_db;
create table products (pid int primary key, pname varchar(32), category varchar(32), price float);

INSERT INTO products VALUES
(1, 'Laptop', 'Electronic', 65000),
(2, 'Sofa', 'Furniture', 20000),
(3, 'Mobile', 'Electronic', 25000),
(4, 'Dining Table', 'Furniture', 18000),
(5, 'Smart TV', 'Electronic', 45000),
(6, 'Chair', 'Furniture', 2500),
(7, 'Headphones', 'Electronic', 3000),
(8, 'Bed', 'Furniture', 30000),
(9, 'Keyboard', 'Electronic', 1500),
(10, 'Cupboard', 'Furniture', 15000);

select * from products;

select sum(price) as total from products;
select category, sum(price) as Total from products group by category;
select category, sum(price) as total from products group by category having total > 1000000;

alter table products add column discount float;

alter table products drop column discount;
select * from products;

alter table products modify column price int;
desc products;

alter table products change column price mrp varchar(32);
select * from products;

alter table products rename to product_details;
select * from product_details;

#Delete
delete from product_details where pname="laptop";

#Truncate
truncate table product_details;

# Drop
drop table product_details;