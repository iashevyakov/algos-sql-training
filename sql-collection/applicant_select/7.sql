SELECT name_department, name_program, plan, COUNT(*) as 'Количество', ROUND(COUNT(*)/plan, 2) as 'Конкурс'
FROM department
JOIN program USING (department_id)
JOIN program_enrollee USING (program_id)
GROUP BY name_department, name_program, plan
ORDER BY 5 DESC