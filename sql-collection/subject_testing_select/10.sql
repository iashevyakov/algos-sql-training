SELECT name_subject, attempt_id
FROM subject
JOIN attempt USING (subject_id)
JOIN testing USING (attempt_id)
JOIN answer USING (answer_id)
GROUP BY name_subject, attempt_id
HAVING SUM(answer.is_correct) = COUNT(answer.answer_id)
ORDER BY name_subject