# Practice session on Functions

create database fun_practice_db;
use fun_practice_db;

create table employee (
    empid int primary key,
    empname varchar(50),
    department varchar(30),
    salary decimal(10,2),
    bonus decimal(10,2),
    experience int,
    attendance int,
    gender varchar(10),
    city varchar(30),
    rating decimal(3,1)
);

INSERT INTO Employee VALUES
(101,'Amit','IT',50000,5000,2,95,'Male','Pune',4.2),
(102,'Priya','HR',45000,4000,3,92,'Female','Mumbai',4.5),
(103,'Rohit','IT',60000,7000,5,98,'Male','Pune',4.8),
(104,'Neha','Sales',40000,3000,1,85,'Female','Nashik',3.9),
(105,'Karan','Finance',55000,6000,4,96,'Male','Pune',4.6),
(106,'Sneha','IT',65000,8000,6,99,'Female','Mumbai',4.9),
(107,'Ajay','Sales',42000,3500,2,88,'Male','Nagpur',4.0),
(108,'Pooja','HR',48000,4500,3,93,'Female','Pune',4.3),
(109,'Rahul','Finance',70000,9000,8,97,'Male','Mumbai',4.7),
(110,'Anjali','IT',58000,5500,4,94,'Female','Pune',4.4);

select * from employee;

-- create function cal_annual_salary(salary float)
-- returns float 
-- deterministic
-- begin
-- 	return salary * 12;
-- end

select empname, cal_annual_salary(salary) from employee;

-- create function total_income(salary float, bonus float)
-- returns float
-- deterministic
-- begin
-- 	return salary+bonus;
-- end

select empname, total_income(salary,bonus) from employee;

-- create function yearly_income(salary float, bonus float)
-- returns float
-- deterministic
-- begin
-- 	return (salary*12)+bonus;
-- end

select empname, yearly_income(salary,bonus) from employee;

-- create function emp_grade(rating float)
-- returns varchar(32)
-- deterministic
-- begin
-- 	if rating >= 4.8 then
-- 		return "Excellent";
-- 	elseif rating >= 4.5 then
-- 		return "Very Good";
-- 	elseif rating >= 4.0 then
-- 		return "Good";
-- 	else
-- 		return "Average";
-- 	end if;
-- end

select empname, emp_grade(rating) from employee;

-- create function attendance_status(att float)
-- returns varchar(32)
-- deterministic
-- begin
-- 	if att >= 95 then
-- 		return "Excellent";
-- 	elseif att >= 90 then
-- 		return "Good";
-- 	elseif att >= 80 then
-- 		return "Average";
-- 	else
-- 		return "Poor";
-- 	end if;
-- end

select empname, attendance_status(attendance) from employee;

-- create function experiance_level(exp int)
-- returns varchar(16)
-- deterministic
-- begin
-- 	if exp >= 8 then
-- 		return "Senior";
-- 	elseif exp >= 5 then
-- 		return "Mid-Level";
-- 	else 
-- 		return "Junior";
-- 	end if;
-- end

select empname, attendance_status(attendance) from employee;

-- create function increment(salary float, inc float)
-- returns float
-- deterministic
-- begin
-- 	return salary * inc/100;
-- end

select empname, increment(salary,10) from employee;

-- CREATE FUNCTION `tax_cal` (salary float)
-- RETURNS float
-- deterministic
-- BEGIN
-- 	declare tax float;
--     if salary > 60000 then
-- 		set tax = salary * 0.20;
-- 	elseif salary > 50000 then
-- 		set tax = salary * 0.1;
-- 	else
-- 		set tax = salary*0.05;
-- 	end if;
--     return tax;
-- END

select empname, salary, tax_cal(salary) from employee;

-- CREATE FUNCTION `net_sal` (salary int)
-- RETURNS INTEGER
-- deterministic
-- BEGIN
-- 	declare ns int;
-- 	declare tax int;
--     set tax = tax_cal(salary);
--     set ns = salary - tax;
--     return ns;
-- END

select empname, salary, tax_cal(salary), net_sal(salary) from employee;

-- CREATE FUNCTION `eligible_emp` (exp int, rating float)
-- RETURNS varchar(16)
-- deterministic
-- BEGIN
-- 	if exp>=3 and rating>=4.5 then
-- 		return "Eligible";
-- 	else	
-- 		return "Not Eligible";
-- 	end if;
-- END

select empname, eligible_emp(experience, rating) from employee;

-- CREATE FUNCTION `work_location` (city varchar(20))
-- RETURNS varchar(20)
-- deterministic
-- BEGIN
-- 	if city = "Pune" then
-- 		return "Local Employee";
-- 	else
-- 		return "Outstation Employee";
-- 	end if;
-- END

select empname, work_location(city) from employee;

-- CREATE FUNCTION `gender_display` (name varchar(32), gender varchar(10))
-- RETURNS varchar(32)
-- deterministic
-- BEGIN
-- 	if gender = "Female" then 
-- 		return concat("Ms.", name);
-- 	elseif gender = "Male" then
-- 		return concat("Mr.", name);
-- 	else
-- 		return name;
-- 	end if;
-- END

select gender_display(empname,gender) from employee;

-- create function performance_score(rating float, att int)
-- returns float
-- deterministic
-- begin
-- 	declare score float;
--     set score = (rating*20) + (att/2);
--     return score;
-- end

select empname, performance_score(rating, attendance) from employee;

-- CREATE FUNCTION `promotion_eligiblity` (exp int, rating float, att int)
-- RETURNS varchar(16)
-- deterministic
-- BEGIN
-- 	if exp >= 5 and rating >=4.5 and att >= 95 then
-- 		return "Promotion Eligible";
-- 	else
-- 		return "Not Eligible";
-- 	end if;
-- END

select empname, promotion_eligiblity(experience,rating,attendance) from employee;