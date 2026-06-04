alter table person_info add constraint pk_pid primary key (pid);

create database oneplus_db;
 use oneplus_db;
 
 select * from mobile_data;
 
 alter table mobile_data add constraint pk_model_no primary key (model_no);
 alter table mobile_data add constraint f_cid foreign key(cid) references student(sid);
 alter table moble_data add constraint ck check (price>0);
 
 alter table mobile_data modify column model_name varchar(32) not null;
 alter table mobile_data modify column ram varchar(16) default '4 GB';
 
 
 select * from students;
 
 create table courses (cid int primary key, cname varchar(32) not null);
 
 create table student_details (roll int primary key auto_increment, name varchar(16) not null, cid int, 
 foreign key (cid) references courses(cid), marks float);
 
 select * from student_details where cid = (select cid from courses where cname="DS");
 select * from student_details where cid in (select cid from courses where cname in ("DS","DW"))
 
select * from student_details where marks > 80;
select * from student_details where cid = (select cid from courses where cname="da");
select * from student_details where cid in (select cid from courses where cname!="da");
  
 select avg(marks) from student_details;
 select marks from student_details where marks >= (select avg(marks) from student_details);
 select * from student_details where marks = (select max(marks) from student_details where cid = (select cid from courses where cname="da"))