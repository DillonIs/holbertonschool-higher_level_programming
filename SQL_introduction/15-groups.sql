-- Count the duplicate scores
SELECT score, COUNT(name) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;