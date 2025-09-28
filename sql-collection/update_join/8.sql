DELETE FROM author
USING
author INNER JOIN supply ON author.name_author=supply.author;