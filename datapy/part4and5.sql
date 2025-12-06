/*1 (date func/operators/and)*/ 
select atmId as "ATM Number",year('2018-01-01') as year, month('2018-01-01') as month, day('2018-01-01') as day
from bankmodel.atm
where cashCapacity > 150000
and statusId != 1;
/*2(in/between)*/ 
select firstName as "Name", lastName as "Surname" 
from bankmodel.customer
where citizenshipId in (1, 3)
and dateOfBirth between '1969-01-20' and '1982-04-18';
/*3 (numeric/like) */ 
select `description`, code, abs(-15.99) as "Reverse amout"
from bankmodel.transaction
where description like'n%';
/*4 (ifnull/orderby)*/
select firstName as "Name", lastName as "Surname", ifnull(dateleft, "employee is still working") as "Last day"
from bankmodel.employee
order by name;
/*5(is,distinct,string func)*/
select distinct branchId as "Branch Number", firstName as "First name", char_length(firstName) as "First name Length"
from bankmodel.employee
where dateLeft is not null;

/*6(inner join)*/
select b.customerId, b.accountId
from bankaccount b
inner join customer c
on b.customerId = c.customerId;

/*7 (inner with more than 2)*/
select b.accountId, l.loanId, t.amount, c.firstName, c.lastName
from bankaccount b
inner join loan l 
on b.accountId = l.accountId
inner join transaction t
on b.accountId = t.accountId
inner join customer c
on b.customerId = c.customerId;

/*8(left outer join)*/
select b.branchId, b.address, c.name as cityName
from branch b
left join city c
on b.cityId = c.cityId
order by c.name;

/*9(right join)*/
select e.employeeId, e.firstName, e.lastName, e.positionId, d.departmentId, d.name as departmentName
from employee e
right join department d
on e.departmentId = d.departmentId
order by d.name, e.lastName;

/*10(inner join)*/
select e.employeeId, e.firstName, e.lastName, d.name as "Deparment name", b.name "Branch Name"
from employee e
inner join branch b
on e.branchId = b.branchId
inner join department d
on e.departmentId = d.departmentId