-- 9. Cities by States
-- A script that lists all cities contained in the database.

SELECT c.id, c.name, s.name
FROM cities AS c INNER JOIN states AS s
ON c.states_id = s.id
ORDER BY c.id;
