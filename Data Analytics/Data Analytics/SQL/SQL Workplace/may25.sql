-- Operators : Operators are the special symbols or keywords used for perform operaions on data
-- There are four types of operatir in sql
-- 1) Arithmetic : Used to perform mathematical calculations.
-- 2) Comparision
-- 3) Logical
-- 4) Special

use employee_db;
select * from emp_details;

-- Arithmetic Opeartors
select emp_id, name, salary+2000 as new_sal from emp_details;
select emp_id, name, salary-1000 from emp_details;
select emp_id, name, salary*5/100 as increment from emp_details;

-- Comparision Operators 
select * from emp_details where dept= "DA";
select * from emp_details where dept != 'HR';
select * from emp_details where salary >= 50000;
select * from emp_details where emp_id < 110;
select * from emp_details where city = "Kolhapur";

-- Logical Operators
select * from emp_details where salary >= 50000 and salary <= 100000;

-- Special Operators
select * from emp_details where dept in ('sales','DA','Testing'); -- in operator
select * from emp_details where salary between 10000 and 45000; -- between operator
select * from emp_details where name like 'A%'; -- like operator
select * from emp_details where name like '_a%';
select * from emp_details where name like '%patil';
select * from emp_details where name like '%t__';
select * from emp_details where name like '%jagtap';
select * from emp_details where name like '__s%';
select * from emp_details where name like '%y%';
select * from emp_details where name like '_o%';

# Aggrigate function -- used to perform calculation on multiple rows and return a single value. Used for reports, analysis and dashboard
-- Example :- max, min, avg, count,sum

select count(*) as Total_Employee from emp_details;
select count(emp_id) as Total_Employee from emp_details;
select count(distinct dept) from emp_details;
select sum(salary) as Total_Salary from emp_details;
select sum(salary) from emp_details where dept="DA";
select max(salary) as maximum_salary from emp_details;
select name from emp_details where salary = (select max(salary) from emp_details);
select min(salary) as minimum_salary from emp_details;
select name from emp_details where salary = (select min(salary) from emp_details);
select avg(salary) from emp_details where dept='DA';

-- group by clause : Group by is used to group rows that have same values in column and mostly used with aggrigate function.
select dept, sum(salary) from emp_details group by dept;
select dept, count(emp_id) as total_emp from emp_details group by dept;
select city, count(emp_id) from emp_details group by city;

select name from emp_details where emp_id = 140;