SELECT name_city, name_author, DATE_ADD('2020-01-01', INTERVAL FLOOR(RAND() * 365) DAY) as 'Дата'
FROM city, author
ORDER BY 1, 3 DESC;