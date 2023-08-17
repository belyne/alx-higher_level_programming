-- Task 8. Cities of California

-- This script lists all the cities of California from the hbtn_0d_usa database.
-- The states table contains only one record where name = California.
-- Results are sorted in ascending order by cities.id.

-- Select the cities of California using a subquery
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
