-- Task 20: Temperatures #2
-- Author: Belyne
-- Date: Current date

-- Use the specified database
USE hbtn_0c_0;

-- Display the max temperature of each state ordered by state name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
