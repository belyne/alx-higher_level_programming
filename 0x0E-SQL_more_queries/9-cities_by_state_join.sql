-- List all cities with their corresponding states in ascending order by cities.id and states.name.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC, states.name ASC;
