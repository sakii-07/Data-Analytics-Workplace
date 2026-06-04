use employee_db;

create table student (sid int primary key, name varchar(32), course varchar(32), per float);

insert into student value(1,"Sakshi","Python Full Stack",89.4),(2,"Divya","Java Full Stack",70),(3,"Amruta","Data Analytics",67.89);

select * from student;
