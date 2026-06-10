-- Trigger Tasks

-- Task 1: Prevent Negative Salary
-- Before Insert
-- If salary < 0
-- Set salary = 0

delimiter $$
create trigger prevent_neg_sal before insert on employee
for each row
begin
	if new.salary < 0 then
		set new.salary = 0;
	end if;
end $$
delimiter ;


-- Task 2: Salary Update Log
-- Whenever salary changes:
-- Store old salary, new salary and update time in Salary_Log table.

create table salary_log (id int primary key auto_increment, old_sal float, new_sal float);

delimiter $$
create trigger update_log after update on employee
for each row 
begin
	insert into salary_log (old_sal,new_sal) values (old.salary, new.salary);
end $$
delimiter ;

-- Task 3: Employee Delete Log
-- Whenever an employee is deleted:
-- Store
-- Employee ID
-- Employee Name
-- Deleted Date
-- in Employee_Delete_Log table.
create table emp_delete_log (id int primary key auto_increment,emp_id int, name varchar(32), del_date timestamp);

delimiter $$
create trigger delete_log after delete on employee
for each row
begin
	insert into emp_delete_log(emp_id, name, del_date) values(old.empid,old.empname,now());
end $$
delimiter ;

-- Task 4: Auto Joining Date
-- Before Insert
-- If joining date is NULL
-- Store current date automatically.

delimiter $$
create trigger auto_joining_date before insert on employee
for each row
begin
	if new.join_date is null then
		set new.join_date = now();
	end if;
end $$
delimiter ;

-- Task 5: Bonus Validation
-- Before Insert
-- If bonus is negative
-- Set bonus = 0

delimiter $$
create trigger bonus_validation before insert on employee
for each row
begin
	if new.bonus < 0 then
		set new.bonus = 0;
	end if;
end $$
delimiter ;

-- Task 6: Attendance Audit
-- Whenever attendance changes:
-- Store old attendance, new attendance and date in Attendance_Log table.

create table Attendance_Log (id int primary key auto_increment, old_att int, new_att int, log_date datetime);

delimiter $$
create trigger attendance_audit before update on employee
for each row
begin
	insert into Attendance_Log (old_att,new_att,log_date) values(old.attendance, old.attendance,now());
end $$
delimiter ;

-- Task 7: Prevent Employee Deletion
-- If employee salary > 100000
-- Do not allow deletion.
-- Show message:
-- High Salary Employee Cannot Be Deleted

delimiter $$ 
create trigger prevent_emp_deletion before delete on employee
for each row
begin
	if old.salary > 100000 then
		SIGNAL SQLSTATE '45000'
		set MESSAGE_TEXT  =  "High Salary Employee Cannot Be Deleted";
        end if;
end $$
delimeter ;

-- Task 8: Department Change Log
-- Whenever department changes:
-- Store
-- Employee ID
-- Old Department
-- New Department
-- Changed Date

create table dept_change_log (id int primary key auto_increment,emp_id int, old_dept varchar(32), new_dept varchar(32),update_date datetime);

delimiter $$
create trigger dept_update_log after update on employee
for each row 
begin
	insert into dept_change_log (emp_id,old_dept,new_dept,update_date) values (old.empid,old.department, new.department,now());
end $$
delimiter ;

-- Task 10: Employee Registration Log
-- Whenever a new employee is inserted:
-- Store record in Audit table:
-- Employee ID
-- Action = INSERT
-- DateTime

create table insert_emp_log (id int primary key auto_increment, emp_id int, action varchar(16), insert_date datetime);

delimiter $$
create trigger emp_insert_log1 after insert on employee
for each row 
begin
	insert into insert_emp_log (emp_id,action,insert_date) values (new.empid, "Insert",now());
end $$
delimiter ;

INSERT INTO Employee VALUES
(113,'gayatri','Sales',20000,1000,3,99,'female','Pune',3.2);