
SELECT author, SUM(price * amount) as 'Стоимость', ROUND(SUM(price * amount) * 0.18 /1.18 ,2) as 'НДС', ROUND(SUM(price * amount)/1.18 ,2) as 'Стоимость_без_НДС'
FROM book
GROUP by author;