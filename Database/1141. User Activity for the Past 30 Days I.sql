SELECT
    a.activity_date AS day,
    COUNT(DISTINCT a.user_id) AS active_users
FROM Activity AS a
WHERE a.activity_date > DATEADD(DAY, -30, '2019-07-27')
GROUP BY a.activity_date 
