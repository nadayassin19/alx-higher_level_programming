-- 9. Cities by States
-- A script that lists all cities contained in the database.

FROM cities
JOIN states ON cities.state_id = states.id
SELECT cities.id, cities.name, states.name;
