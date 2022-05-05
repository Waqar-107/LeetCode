SELECT w1.id
FROM Weather AS w1
INNER JOIN Weather AS w2 ON DATEDIFF(DAY, w2.recordDate, w1.recordDate) = 1
AND w1.temperature > w2.temperature
