-- having clause -- 
use employee_db;
select * from emp_details;

select dept, sum(salary) as 'Total salary' from emp_details group by dept having sum(salary)>500000;
select dept, sum(salary) as Total_salary from emp_details group by dept having Total_salary between 100000 and 400000;


-- Join : Join is used to combine data from two or more tables based on related column. 
-- 		  Tables are connected using primary key or foriegn key
-- Q. Need of Join
-- In a real databases data is not stored in one table, data is split into multiple tables
-- Join help us to get combine information
-- 		Types of join --
-- 				   1) Inner Join
--                 2) Left Join
--                 3) Right Join
--                 4) Cross Join
--                 5) Full Join

create database Institude_db;
use Institude_db;

select * from courses;
select * from student_admission;
select * from student_marks;

-- Inner Join
select student_admission.sid, name, city, test1_marks, test2_marks from student_admission inner join 
student_marks on student_admission.sid=student_marks.sid;

-- Left Join : all records from left table amd matching records from right table
select student_admission.sid, name, city, test1_marks, test2_marks from student_admission left join 
student_marks on student_admission.sid=student_marks.sid;

-- Right Join : all records from right table amd matching records from left table
select student_admission.sid, name, city, test1_marks, test2_marks from student_admission right join
student_marks on student_admission.sid = student_marks.sid;

select student_marks.sid, name, city, test1_marks, test2_marks from student_admission right join
student_marks on student_admission.sid = student_marks.sid;