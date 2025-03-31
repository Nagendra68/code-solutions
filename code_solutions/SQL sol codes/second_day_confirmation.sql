SELECT user_id
FROM emails  e join texts t on e.email_id = t.email_id
where t.action_date = e.signup_date + INTERVAL '1 day'

;