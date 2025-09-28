UPDATE book INNER JOIN author USING (author_id) INNER JOIN supply ON book.title=supply.title AND supply.author=author.name_author
SET book.amount=book.amount+supply.amount,
    book.price=(book.price*book.amount+supply.price*supply.amount) / (book.amount+supply.amount),
    supply.amount=0
WHERE book.price!=supply.price;