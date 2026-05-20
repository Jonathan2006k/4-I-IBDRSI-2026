# Write your MySQL query statement below
with RankedSalaries as (
    select
    d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    DENSE_RANK() over(
        partition by e.departmentId
        order by e.salary desc
    ) as salary_rank
    from Employee e
    Join Department d on e.departmentId = d.id
)
select 
Department,
Employee,
Salary
from RankedSalaries
where salary_rank <= 3;
