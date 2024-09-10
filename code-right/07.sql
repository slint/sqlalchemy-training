
SELECT id, email, ... FROM users WHERE email = '?' LIMIT 1;



SELECT id, email, ... FROM users WHERE email = '?' LIMIT 1;







-- We begin a transaction explicitly
BEGIN;


UPDATE users
SET
  quota = ???  -- QUIZ❓: What's the value?
WHERE  -- QUIZ❓: What's the condition?
  ???;

UPDATE user_profile
SET
  system_info = '{"vip": true}'
WHERE
  ???;

COMMIT;

-- QUIZ❓: When exactly did all this SQL actually happen?
