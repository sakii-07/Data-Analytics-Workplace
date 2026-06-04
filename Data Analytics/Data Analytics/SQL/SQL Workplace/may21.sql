use db_1;
Select * from details;

create database employee_db;

show databases;
use employee_db;

create table emp_details (emp_id int, name varchar(32),city varchar(16), dept varchar(16), salary int);

desc emp_details;

insert into emp_details values (101,"Sakshi JAgtap","Solapur","Dev",60000);

insert into emp_details (emp_id,name,city,salary) values (102,"Sojar Gaikwad","Sangola",40000);

insert into emp_details values (103,"Shital Sutar","Pune","Testing",340000),(104,"Amruta Patil","Solapur","DA",45000);

select * from emp_details;

-- DQL commands -- 
-- 	1) select
-- Examples :- 
-- 	select * from table_name;
--     select col1, col2, col3  from t_name;

insert into emp_details values
(105,"Rahul Patil","Nagpur","Developer",68000),
(106,"Sneha Joshi","Nashik","Testing",52000),
(107,"Vikas More","Kolhapur","HR",47000),
(108,"Neha Kulkarni","Mumbai","DA",62000),
(109,"Rohan Jadhav","Pune","Developer",81000),
(110,"Kiran Pawar","Satara","Support",40000),
(111,"Anjali Mehta","Aurangabad","Testing",56000),
(112,"Sagar Shinde","Thane","Developer",90000),
(113,"Pooja Patil","Solapur","HR",48000),
(114,"Nitin Kale","Nagpur","Support",42000),
(115,"Komal Chavan","Pune","DA",67000),
(116,"Akash More","Mumbai","Developer",95000),
(117,"Reshma Patil","Nashik","Testing",53000),
(118,"Yogesh Mane","Kolhapur","Support",39000),
(119,"Swati Jagtap","Satara","HR",51000),
(120,"Omkar Deshmukh","Aurangabad","Developer",88000),
(121,"Deepak Salunkhe","Pune","Testing",59000),
(122,"Rutuja More","Mumbai","DA",72000),
(123,"Manoj Shinde","Solapur","Support",41000),
(124,"Vaishnavi Patil","Nagpur","Developer",83000);

select * from emp_details;

-- Where Clause :- used for filter records based on condition 
-- Syntax :- select * from t_name where conditon

select * from emp_details where dept="Developer";
select * from emp_details where salary < 50000;
select name from emp_details where salary >= 30000 and salary <= 50000;
select * from emp_details where dept="Developer" and salary <= 70000;
select * from emp_details where dept="Support" or dept="HR";

-- create table course deatils
create table course_details(cid int,c_name varchar(32),duration int,fees float,trainer varchar(32));

insert into course_details values (1,"Java",6,20000,"Mayur sir"),
(2,"Python",6,32000,"Atul sir"),
(3,"DA",6,25000,"Vaibhav sir"),
(4,"DS",6,40000,"Ritik sir"),
(5,"Testing",6,15000,"Atul sir");

select * from course_details;