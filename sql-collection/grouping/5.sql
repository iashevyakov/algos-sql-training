SELECT MIN(price) as 'Минимальная_цена', MAX(price) as 'Максимальная_цена', ROUND(AVG(price),2) as 'Средняя_цена'
FROM book;