/*single row subq*/
select *
from bankmodel.department
where departmentId = 
	(select departmentId
    from bankmodel.department
    where name = "Marketing"
    and regionId = 1)
;

/*multiple row subq*/
select e.firstName as "First Name", e.lastName as "Last Name", p.Name as "Role"
from bankmodel.employee e
join bankmodel.position p
on e.positionId = p.positionId
where e.employeeId in
	(select employeeId
    from bankmodel.employee
    where month(dateHired) = 5)
;

/*double key subq*/
select *
from bankmodel.customer
where nationalityId in
	(select nationalityId
    from bankmodel.customer
    where nationalityId = 1)
and genderId in
	(select genderId
    from bankmodel.customer
    where genderId = 1)
;

/*nested subq*/
select *
from bankmodel.branch
where cityId in
    (select cityId
     from bankmodel.city
     where regionId in
        (select regionId
         from bankmodel.region
         where regionId = 3))
;

/*subq in selected*/
select employeeId, firstName, lastName, salary,
    (select avg(salary) 
    from bankmodel.employee) as Company_Avg_Salary
from Employee
where salary < 
    (select avg(salary)
    from Employee)
order by salary desc;

/*setfunction 1*/
select atmId, currentCashAmount,
	(select sum(currentCashAmount)
    from bankmodel.atm
    where currentCashAmount > 55000)
FROM bankmodel.atm
WHERE currentCashAmount > 10000
ORDER BY currentCashAmount ASC;

/*setfunction 2*/
select accountId, count(amount) as "amount"
from bankmodel.transaction
where accountId in
	(select accountId
    from bankmodel.transaction
    where description like '%c%')
group by accountId
order by count(amount) asc;