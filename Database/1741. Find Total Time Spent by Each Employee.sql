SELECT
    e.event_day AS day,
    e.emp_id AS emp_id,
    (SUM(e.out_time) - SUM(e.in_time)) AS total_time
FROM Employees e
GROUP BY e.emp_id, e.event_day
