-- Write your PostgreSQL query statement below
select x,y,z,
case
    When x+y>z and y+z>x and x+z>y then 'Yes' else 'No'
    end as triangle
from Triangle;

