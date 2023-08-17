-- Task 19: Temperatures #1
-- Author: Belyne
-- Date: Current date

-- Use the specified database
USE hbtn_0c_0;

-- Display the top 3 cities' temperatures during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
