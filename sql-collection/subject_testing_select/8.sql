SELECT name_student, name_subject, date_attempt, ROUND(SUM(IF(is_correct=true, 1, 0)) / 3 * 100, 2) as 'Результат'
FROM student
JOIN attempt USING (student_id)
JOIN subject USING (subject_id)
JOIN testing USING (attempt_id)
JOIN answer USING (answer_id)
GROUP BY name_student, name_subject, date_attempt
ORDER BY name_student, date_attempt DESC