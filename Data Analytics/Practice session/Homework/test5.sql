As a user, I want to add an column branch_location so I can
efficiently search the branch wise record.
2. As a user, I want to check the total salary expenses on employees.
3. As a user, I want to see the max salary of employee from test
profile.
4. As a user I want to get the average experience level of employees.
5. As a user I want to see the name of highest paid employee.
6. As a user, I want to see the name and experience of lowest paid
employee.
7. As a user I want check how many employees are working in
company.
8. As a user I want to see those employee names who are from test
profile and having salary more than 25K.
9. As a user, I want to shift Radha on support profile.
10. As a user, I want to get the second highest salary of employee.
11. As a user I want to get the second lowest salary of employee.
12. As a user, I want to calculate the average salary of employees
those are belongs to dev profile.
13. As a user, I want to see the employee’s name and salary who is
having lowest experience.
14. As a user, I want to see the employee name who is having lowest
age with max salary.
15. As a user, I want to remove all the employee from company.







table employee [id,name,role,salary]
----------------------------------------
1. Print employee name & role those role is Tester.
2. Print all those role is Dev and salary is above 50,000
3. Print count those role is Tester**
4. Print count those salary is above 60,000
5. Print employees those name starts as "R" 
6. Print employees as ascending order on basis of name
7. Print employees as descending order on basis of salary
8. Print employee who having highest salary
9. Print total salary company paid to Testers
10.Update salary as 10% those role is Tester

Answers 

SELECT *  FROM db_1213.employee;
SELECT name,role  FROM db_1213.employee where role = 'Tester';
SELECT * FROM db_1213.employee where role = 'Dev' AND salary > 50000;

SELECT count(*) FROM db_1213.employee where role = 'Tester' ;

SELECT count(salary>50000) FROM db_1213.employee;
SELECT *  FROM db_1213.employee where name like ('R%')  ;
SELECT *  FROM db_1213.employee order by name; 
SELECT *  FROM db_1213.employee order by salary desc ; 

SELECT sum(salary) FROM db_1213.employee where role = 'Tester';

SELECT max(salary) FROM db_1213.employee;

SELECT *  FROM db_1213.employee  where salary = (
	SELECT max(salary) FROM db_1213.employee) ;

SELECT *  FROM db_1213.employee  order by salary desc limit 1;

SELECT *  FROM db_1213.employee  order by salary desc limit 1 offset 1;

select salary FROM db_1213.employee where id = 2 ;

update db_1213.employee set salary  = salary + (salary * 10 / 100) where role = 'Tester'  ; 