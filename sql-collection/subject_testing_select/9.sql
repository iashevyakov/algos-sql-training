SELECT name_subject, CONCAT(LEFT(name_question, 30), '...') as 'Вопрос', COUNT(answer.answer_id) as 'Всего_ответов',
ROUND(SUM(answer.is_correct) / COUNT(answer.answer_id) * 100, 2) as 'Успешность'
FROM subject
JOIN question USING (subject_id)
JOIN testing USING (question_id)
JOIN answer USING (answer_id)
GROUP BY name_subject, name_question
ORDER BY 1, 4 DESC, name_question
