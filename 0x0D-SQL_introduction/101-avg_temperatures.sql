-- Task 18: Temperatures #0
-- Author: Belyne
-- Date: Current date

-- Use the specified database
USE hbtn_0c_0;

-- Display average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, ROUND(AVG(value), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
