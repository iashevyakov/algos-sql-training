SELECT book.title as 'Название', name_author as 'Автор', book.amount + supply.amount as 'Количество'
FROM author INNER JOIN book USING(author_id)
INNER JOIN supply ON author.name_author=supply.author AND book.title=supply.title AND book.price=supply.price;