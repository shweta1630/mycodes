-- Write your PostgreSQL query statement below

select m.employee_id,
    m.name,
    count(e.employee_id) as reports_count,
    round(avg(e.age))as average_age
from employees m
join employees e
on e.reports_to is not null
and e.reports_to=m.employee_id
group by m.employee_id,m.name
order by m.employee_id;
