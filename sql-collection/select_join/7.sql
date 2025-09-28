SELECT title, name_author, name_genre, price, amount
FROM author
INNER JOIN book ON author.author_id=book.author_id
INNER JOIN genre ON book.genre_id=genre.genre_id
WHERE genre.genre_id IN
(SELECT query_1.genre_id FROM
(SELECT genre_id, sum(amount) as sum_amount FROM book GROUP BY genre_id) as query_1
INNER JOIN
(SELECT genre_id, sum(amount) as sum_amount FROM book GROUP BY genre_id ORDER BY 2 DESC LIMIT 1) as query_2
ON query_1.sum_amount=query_2.sum_amount
 )
ORDER BY title;