-- Q. create a table with name student marks, columns like rollno name tast1 test2 test3 and 5 records
-- create table
create table student_marks (roll int, name varchar(32), test1 int, test2 int, test3 int);

-- insert records
insert into student_marks values(1,"Sakshi Jagtap",98,78,89),(2,"Sojar Gaikwad",78,56,84),
(3,"Shital Sutar",80,68,72),(4,"Pranjali Gaikwad",71,90,67),(5,"Amruta Patil",67,82,61);

-- fetch records
select * from student_marks;

-- +------+------------------+-------+-------+-------+
-- | roll | name             | test1 | test2 | test3 |
-- +------+------------------+-------+-------+-------+
-- |    1 | Sakshi Jagtap    |    98 |    78 |    89 |
-- |    2 | Sojar Gaikwad    |    78 |    56 |    84 |
-- |    3 | Shital Sutar     |    80 |    68 |    72 |
-- |    4 | Pranjali Gaikwad |    71 |    90 |    67 |
-- |    5 | Amruta Patil     |    67 |    82 |    61 |
-- +------+------------------+-------+-------+-------+