/*1*/
select c.customerId, c.firstName, c.lastName,
	(select count(*)
    from bankmodel.bankaccount b
    where b.customerId = c.customerId) as Accountcount,
    (select count(*)
    from bankmodel.transaction t
    where t.accountId in (
		select ba.accountId
        from bankmodel.bankaccount ba
        where ba.customerId = c.customerId)
        ) as Transactioncount
from bankmodel.customer c
order by transactioncount desc;

/*2*/
select c.customerId, c.firstName, c.lastName,
	(select round(sum(b.balance), 2)
    from bankmodel.bankaccount b
    where b.customerId = c.customerId) as totalbalance
from bankmodel.customer c
order by totalbalance asc;

/*3*/
select a.atmId, a.brandId, a.currentCashAmount
from bankmodel.atm a
where a.currentCashAmount >
	(select avg(`at`.currentCashAmount)
    from bankmodel.atm at
    where a.brandId = `at`.brandId)
order by currentCashAmount;

/*group by with one or more set functions*/
select statusId, count(*) as "ATM count", ROUND(100 * COUNT(*) / (SELECT COUNT(*) FROM bankmodel.ATM), 2) AS "percantage"
from bankmodel.atm
group by statusId;

/*group by on multiple columns*/
select departmentId, positionId, COUNT(*) as "Employee Count"
from bankmodel.employee
group by departmentId, positionId
order by departmentId, positionId;

/*group by with an expression*/
select date(dateTime) as "Transaction Date", COUNT(*) as transactionCount
from bankmodel.transaction
group by date(dateTime)
order by transactionDate;

/*having 1*/
select date(dateTime) as "Transaction Date", count(*) as "Transaction Count", sum(amount) as total
from bankmodel.transaction
group by date(dateTime)
having sum(amount) > 1000
order by total asc;

/*having 2*/
select year(startDate) as loanyear, count(*) as "Loan count"
from bankmodel.loan
group by year(startDate)
having count(*) >= 2
order by loanyear;