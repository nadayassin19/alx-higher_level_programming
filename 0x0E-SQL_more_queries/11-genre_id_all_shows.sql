-- 11. Genre ID for all shows
-- A script that lists all shows contained in a database.

FROM tv_shows AS s LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id
SELECT s.title, g.genre_id;
