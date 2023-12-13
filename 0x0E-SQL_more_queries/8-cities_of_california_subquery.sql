-- 8. Cities of California
-- A script that lists all the cities of a specific state that can be found in a database.

FROM cities
SELECT id, name
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
);
