SELECT
    f.user_id AS user_id,
    COUNT(f.follower_id) AS followers_count
FROM Followers AS f
GROUP BY f.user_id
