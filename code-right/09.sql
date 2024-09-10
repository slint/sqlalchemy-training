SELECT
  SUM(up.quota)
FROM
  user_profile as up
  JOIN users as u ON up.user_id = u.id
WHERE
  up.system_info->>'vip' = 'true'
ORDER BY up.quota DESC
LIMIT 10;
