SELECT g.name, count(*) FROM genre g 
JOIN genre_musician gm ON g.genre_id = gm.genre_id 
GROUP BY g.name 
ORDER BY count(*) DESC;

SELECT count(*) FROM album a 
JOIN track t ON a.album_id = t.album_id
WHERE a.year BETWEEN 2019 AND 2020;

SELECT a.name, round(avg(t.length), 2) FROM album a 
JOIN track t ON a.album_id = t.album_id
GROUP BY a.name;

SELECT m.name FROM musician m
WHERE m.name <> (SELECT m.name FROM musician m 
JOIN musician_album ma ON m.musician_id = ma.musician_id
JOIN album a ON ma.album_id = a.album_id
WHERE a.year = 2020 
GROUP BY m.name);

SELECT DISTINCT c.name FROM collection c 
JOIN collection_track ct ON c.collection_id = ct.collection_id 
JOIN track t ON ct.track_id = t.track_id 
JOIN musician_album ma ON t.album_id = ma.album_id
JOIN musician m ON ma.musician_id = m.musician_id 
WHERE m.name = 'Дима Билан'

SELECT DISTINCT a.name FROM album a 
JOIN musician_album ma ON a.album_id = ma.album_id
JOIN musician m ON ma.musician_id = m.musician_id
JOIN genre_musician gm ON m.musician_id = gm.musician_id
GROUP BY a.name, gm.musician_id
HAVING count(genre_id) > 1;

SELECT t.name FROM track t
LEFT JOIN collection_track ct ON t.track_id = ct.track_id
WHERE ct.track_id IS NULL;

SELECT DISTINCT m.name FROM musician m 
JOIN musician_album ma ON m.musician_id = ma.musician_id 
JOIN track t ON ma.album_id = t.album_id 
WHERE t.length = (SELECT min(t.length) FROM track t);

SELECT a.name FROM album a
JOIN track t ON t.album_id = a.album_id
GROUP BY a.name
HAVING COUNT(t.track_id) = (
	SELECT COUNT(t.track_id) FROM track t
	JOIN album a ON a.album_id = t.album_id
	GROUP BY a.name
	ORDER BY COUNT(t.track_id)
	LIMIT 1);