-- 20. Best genre
-- A script that lists all genres in the database hbtn_0d_tvshows_rate,
-- by their rating.

FROM tv_genres AS g INNER JOIN tv_show_genres AS s
ON s.genre_id = g.id
INNER JOIN tv_show_ratings AS r
ON r.show_id = s.show_id
GROUP BY name
ORDER BY rating DESC
SELECT name, SUM(rate) AS rating;