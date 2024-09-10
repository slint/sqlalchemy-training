
SELECT
  email,
  created
FROM users
WHERE
  created >= '2024-03-01'
  AND email LIKE '%@cern.ch'

ORDER BY created DESC
LIMIT 10
