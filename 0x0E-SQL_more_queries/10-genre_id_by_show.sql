-- 10. Genre ID by show
-- A script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

FROM tv_shows AS s INNER JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title, g.genre_id
SELECT s.title, g.genre_id;