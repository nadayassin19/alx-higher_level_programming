-- 8. Cities of California
-- A script that lists all the cities of a specific state that can be found in a database.

SELECT id, name
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id
FROM cities;
