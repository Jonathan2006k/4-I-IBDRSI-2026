# Write your MySQL query statement below
select e.name as Employee
from Employee e
inner Join employee m on e.managerID = m.id
where e.salary > m.salary;
