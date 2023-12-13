-- 15. Only Comedy
-- A script that lists all Comedy shows in the database.

FROM tv_shows AS t INNER JOIN tv_show_genres AS s
ON t.id = s.show_id
INNER JOIN tv_genres AS g
ON g.id = s.genre_id
WHERE g.name = "Comedy"
ORDER BY t.title
SELECT t.title;
