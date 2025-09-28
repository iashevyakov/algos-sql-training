
SELECT author, MIN(price) as 'Минимальная_цена', MAX(price) as 'Максимальная_цена', AVG(price) as 'Средняя_цена'
FROM book
GROUP by author;