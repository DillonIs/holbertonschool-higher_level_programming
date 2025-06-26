-- Script that lists all records where there is a name in second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;