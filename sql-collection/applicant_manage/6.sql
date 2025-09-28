SET @num_pr := 0;
SET @row_num := 1;

UPDATE applicant_order, (
    SELECT *,
     if(program_id = @num_pr, @row_num := @row_num + 1, @row_num := 1) AS str_num,
     @num_pr := program_id AS add_var
    from applicant_order
)  as app_ordered
SET applicant_order.str_id=app_ordered.str_num
WHERE applicant_order.program_id=app_ordered.program_id AND applicant_order.enrollee_id=app_ordered.enrollee_id;