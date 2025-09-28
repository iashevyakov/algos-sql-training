SELECT name_student, name_subject, DATEDIFF(MAX(date_attempt), MIN(date_attempt)) as 'Интервал'
FROM student JOIN attempt USING (student_id) JOIN subject USING (subject_id)
GROUP BY name_student, name_subject
HAVING DATEDIFF(MAX(date_attempt), MIN(date_attempt)) > 0
ORDER BY 3
