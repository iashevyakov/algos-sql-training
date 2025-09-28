SELECT name_author
FROM author INNER JOIN book on author.author_id=book.author_id
GROUP by name_author
HAVING COUNT(DISTINCT(genre_ID))=1
ORDER BY name_author;
