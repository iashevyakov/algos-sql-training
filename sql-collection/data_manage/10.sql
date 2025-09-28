UPDATE book,supply
SET book.price = supply.price, supply.amount = book.amount + supply.amount;