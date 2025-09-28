SELECT author, SUM(price*amount) as 'Стоимость'
FROM book
WHERE title NOT IN ('Идиот', 'Белая гвардия')
GROUP by author
HAVING SUM(price * amount) > 5000
ORDER BY Стоимость DESC;