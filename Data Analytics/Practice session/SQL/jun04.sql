-- Stored Procedure Tasks

-- Task 1: Add New Employee
-- Create a stored procedure that accepts all employee details and inserts a new record into the Employee table.

-- create procedure add_employee(in id int,in name varchar(32),in dept varchar(32), in sal float,in bonus float, in experi int,
-- in att int, in gender varchar(32), in city varchar(32),in rating float)
-- begin
-- 	insert into employee values(id,name,dept,sal,bonus,experi,att,gender,city,rating);
-- end

call add_employee(111,"sakshi jagtap","dev",34000,3400,6,98,'F','Solapur',4.8);

-- Task 2: Department Wise Employees
-- Create a procedure that accepts department name and displays all employees from that department.

-- CREATE PROCEDURE `GetEmployeesByDepartment` (in dept varchar(32))
-- BEGIN
-- 	select * from employee where department=dept;
-- END

CALL GetEmployeesByDepartment('IT');

-- Task 3: Employee Salary Hike
-- Create a procedure that accepts: Employee ID, Hike Percentage and updates the employees salary.

-- CREATE PROCEDURE `SalaryHike` (in id int, in inc float)
-- BEGIN
-- 	update employee set salary = salary + salary*inc/100 where empid = id;
-- END

CALL SalaryHike(101,10);

-- Task 4: Employee Details by ID
-- Create a procedure that accepts Employee ID and displays complete employee information.

-- CREATE PROCEDURE `get_emp_by_id` (in id int)
-- BEGIN
-- 	select * from employee where empid = id;
-- END

call get_emp_by_id(110);

-- Task 5: Employee Count by Department
-- Create a procedure that accepts department name and returns total employees in that department. Use OUT parameter.

-- CREATE PROCEDURE `emp_count_by_department` (in dept varchar(32), out count int)
-- BEGIN
-- 	select count(*) as "Total Employee" from employee group by department having department = dept;
-- END

call emp_count_by_department("IT");

-- Task 6: Calculate Annual Salary
-- Accept Employee ID and return: Employee Name, Monthly Salary, Annual Salary

-- CREATE PROCEDURE `cal_annual_salary` (in id int)
-- BEGIN
-- 	select empname, salary, salary*12 as "Annual salary" from employee where empid=id;
-- END

call cal_annual_salary(111);

-- Task 7: Transfer Employee
-- Accept: Employee ID, New Department, and update the department.

-- CREATE PROCEDURE `update_deptartment` (in id int, in dept varchar(32))
-- BEGIN
-- 	update employee set department = dept where empid = id;
-- END

call update_deptartment(104,"Testing");

-- Task 8: Highest Paid Employee
-- Create a procedure to display highest salary employee details.

-- CREATE PROCEDURE `Highest_paid_emp` ()
-- BEGIN
-- 	select * from employee where salary = (select max(salary) from employee);
-- END

call Highest_paid_emp();

-- Task 9: Bonus Distribution
-- Increase bonus by: Rating >= 4.5 → Bonus + 2000, Otherwise → Bonus + 1000 for all employees.

-- CREATE PROCEDURE `bonus_distribution` ()
-- BEGIN
-- 	update employee set bonus = bonus+200 where rating >= 4.5;
--     update employee set bonus = bonus+1000 where rating < 4.5;
-- END

call bonus_distribution();

-- Task 10: Employee Promotion
-- Accept Employee ID.
-- If: Experience >= 5, Rating >= 4.5 then change designation to: Senior Employee otherwise Not Eligible

-- CREATE PROCEDURE `emp_promotion` ()
-- BEGIN
-- 	update employee set destination = "Senior Employee" where rating >= 4.5 and experinace >= 5;
--     update employee set destination = "Not Eligible" where rating < 4.5 and experinace < 5;
-- END

call emp_promotion();