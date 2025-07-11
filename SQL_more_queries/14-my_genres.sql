-- Lists all genres of a specified show
SELECT name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS m
ON g.id = m.genre_id
INNER JOIN tv_shows AS t
ON m.show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY name ASC;