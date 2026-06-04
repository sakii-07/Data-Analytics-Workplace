-- function 

-- string fuctions
-- upper / ucase
-- lower / lcase
-- concat
-- trim
-- lenght

-- numeric functions
-- round
-- ceil
-- floor
-- mod
-- power

-- date function
-- row
-- current_date
-- date
-- year
-- month
-- date_diff

use student;

desc student_details;

INSERT INTO student_details
(name, age, course_name, admission_date, end_date, obt_marks, total_marks)
VALUES
('Aarav Sharma', 20, 'Java', '2025-01-10', '2025-06-10', 420, 500),
('Priya Patil', 21, 'Python', '2025-02-15', '2025-07-15', 450, 500),
('Rohan Singh', 22, 'SQL', '2025-03-01', '2025-08-01', 390, 500),
('Sneha Joshi', 19, 'Web Development', '2025-01-20', '2025-06-20', 470, 500),
('Aditya Kulkarni', 23, 'Data Science', '2025-02-05', '2025-07-05', 440, 500),
('Neha Verma', 20, 'Java', '2025-03-12', '2025-08-12', 410, 500),
('Rahul Gupta', 21, 'Python', '2025-01-18', '2025-06-18', 430, 500),
('Pooja Deshmukh', 22, 'SQL', '2025-02-22', '2025-07-22', 460, 500),
('Vikram Yadav', 20, 'Web Development', '2025-03-08', '2025-08-08', 400, 500),
('Anjali Mehta', 19, 'Data Science', '2025-01-25', '2025-06-25', 480, 500),
('Karan Shah', 24, 'Java', '2025-02-10', '2025-07-10', 395, 500),
('Meera Nair', 21, 'Python', '2025-03-15', '2025-08-15', 455, 500),
('Arjun Rao', 22, 'SQL', '2025-01-30', '2025-06-30', 425, 500),
('Kavya Iyer', 20, 'Web Development', '2025-02-18', '2025-07-18', 445, 500),
('Siddharth Jain', 23, 'Data Science', '2025-03-05', '2025-08-05', 470, 500),
('Ritika Mishra', 21, 'Java', '2025-01-12', '2025-06-12', 435, 500),
('Yash Patwardhan', 22, 'Python', '2025-02-28', '2025-07-28', 415, 500),
('Tanvi Chavan', 20, 'SQL', '2025-03-20', '2025-08-20', 465, 500),
('Omkar Jadhav', 21, 'Web Development', '2025-01-08', '2025-06-08', 405, 500),
('Shruti Kapoor', 22, 'Data Science', '2025-02-14', '2025-07-14', 490, 500);

select * from student_details;

select upper(name) as upper from student_details;
select lower(name) as lower from student_details;
select concat(name,age) from student_details;
select length(name) from student_details;

select round(obt_marks) from student_details;
select ceil(obt_marks) from student_details;
select floor(obt_marks) from student_details;
select power(roll,2) from student_details;
select mod(roll,2) from student_details;

select current_date() from student_details;
select now() from student_details;
select year(admission_date) from student_details;
select month(admission_date) from student_details;
select day(admission_date) from student_details;
select datediff(end_date,admission_date) from student_details;

# user defined fuctons
-- syntax  
--    create function 'function name'(col datatype)
--    return integer
--    deterministic
--    begin
--          # logic
--          declare var dt;
--          set var = value;
--          return value;
--    end

-- CREATE DEFINER=`root`@`localhost` FUNCTION `square`(num int) RETURNS int
--     DETERMINISTIC
-- BEGIN
-- 	return num*num;
-- END

select square(roll) from student_details;
select roll, name, percentage(obt_marks, total_marks) from student_details;
select name, increment(obt_marks, 5) from student_details;

create table std_percentage as select roll, name, percentage(obt_marks, total_marks) from student_details;

# conditional
--    create function 'function name'(col datatype)
--    return integer
--    deterministic
--    begin
--          # logic
--          declare var dt;
--          if cond then
--          	return value;
--          else
--          	return value;
--          end if
--    end

-- CREATE DEFINER=`root`@`localhost` FUNCTION `result`(marks float, passing_marks float) RETURNS varchar(16) CHARSET utf8mb4
--     DETERMINISTIC
-- begin
-- 	if marks > passing_marks then
-- 		return "PASS";
-- 	else
-- 		return "Fail";
-- 	end if;
-- end

select roll, name, result(obt_marks, 400) from student_details;
select roll, name, iseligible(age) from student_details;

# for multiple condition
--    create function 'function name'(col datatype)
--    return integer
--    deterministic
--    begin
--          # logic
--          declare var dt;
--          if cond then
--          	return value;
--          elseif cond2 the
--				return value;
--          elseif cond3 the
--				return value;
--          else
--          	return value;
--          end if
--    end

-- CREATE DEFINER=`root`@`localhost` FUNCTION `cal_grade`(marks float) RETURNS varchar(8) CHARSET utf8mb4
--     DETERMINISTIC
-- begin

-- 	if marks > 450 then
-- 		return 'A';
-- 	elseif marks > 350 then
-- 		return 'B';
-- 	elseif marks > 250 then
-- 		return 'C';
-- 	else
-- 		return 'D';
-- 	end if;

-- end

select roll, name, cal_grade(obt_marks) from student_details;