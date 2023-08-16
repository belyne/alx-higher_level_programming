-- Task 15: Number by score
-- Author: Belyne
-- Date: Current date

-- List the number of records with the same score and order by the number (descending)
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
