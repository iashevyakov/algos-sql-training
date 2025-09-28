DELETE FROM author
USING
author INNER JOIN book USING (author_id) INNER JOIN genre USING (genre_id)
WHERE name_genre = 'Поэзия';
