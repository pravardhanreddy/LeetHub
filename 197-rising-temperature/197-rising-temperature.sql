# Write your MySQL query statement below
select w.id
from weather q, weather w
where DATE_ADD(w.recordDate, Interval -1 day) = q.recordDate and w.temperature > q.temperature;