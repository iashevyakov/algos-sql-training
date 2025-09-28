FROM city
JOIN client USING (city_id)
JOIN buy USING (client_id)
ORDER BY buy_id