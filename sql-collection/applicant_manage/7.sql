CREATE TABLE student AS
SELECT name_program, name_enrollee, itog FROM (
    SELECT name_program, name_enrollee, itog, plan, ROW_NUMBER() OVER (PARTITION BY program_id) AS row_num
    FROM program
    JOIN applicant_order USING (program_id)
    JOIN enrollee USING (enrollee_id)
) student_numered
WHERE student_numered.row_num<=student_numered.plan
ORDER BY name_program, itog DESC;
