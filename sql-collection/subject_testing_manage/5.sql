DELETE FROM attempt
WHERE subject_id IN
(
    SELECT subject_id FROM subject WHERE name_subject IN ('Основы баз данных', 'Основы SQL')
)
