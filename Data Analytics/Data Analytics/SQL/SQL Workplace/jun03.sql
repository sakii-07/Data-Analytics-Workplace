# View -- A view in SQL is a virtual table that does not store any physical data itself.
-- 		syntax :- create view view_name as (select query);
--      Virtial table that stores query

create view emp_data as select empid, empname, department, attendance, rating from employee;

select * from emp_data;

select * from emp_data where attendance>95;

# Stored procedure :- 

-- create procedure show_all()
-- begin
-- 	select * from employee;
-- end

call show_all();

-- CREATE PROCEDURE `IT_emp` ()
-- BEGIN
-- 	select * from employee where department="IT";
-- END

call IT_emp();

-- CREATE PROCEDURE `get_dep_emp` (in dep varchar(16))
-- BEGIN
-- 	select * from employee where department = dep;
-- END

call get_dep_emp("sales");

-- CREATE PROCEDURE `total_bonus` ()
-- BEGIN
-- 	select sum(bonus) from employee;
-- END

call total_bonus();

-- CREATE PROCEDURE `total_dep_sal` (in dep varchar(16))
-- BEGIN
-- 	select department, sum(salary) from employee group by department having department = dep;
-- END

call total_dep_sal("sales");

# Trigger :- 
-- Syntax -
-- 		create Trigger t_name
-- 		before/after insert/update/delete
-- 		on table_name
-- 		for each row
-- 		begin
-- 			// logic
-- 		end

use employee_db;
select * from emp_details;

delimiter $$
create trigger chk_sal before insert on emp_details
for each row
begin
	if new.salary < 0 then
		set new.salary = 0;
	end if;
end $$
delimiter ;

insert into emp_details values(125,"Divya Jagtap","Solapur","HR",-20000);

select * from emp_details;

delimiter $$
create trigger add_report after insert on emp_details
for each row
begin
	insert into report (msg,date) values("added",now());
end $$
delimiter ;

insert into emp_details values(126,"Durga Jagtap","Sangola","IT",89000);
select * from report;