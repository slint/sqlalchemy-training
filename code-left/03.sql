SELECT
  u.email,
  CASE cm.role
    WHEN 'owner' THEN 'Owner'
    ELSE 'Member'
  END AS community_role,
  DATEPART('year', cm.created) AS joined_year
FROM
  users AS u
  JOIN community_members AS cm ON u.id = cm.user_id
WHERE
  u.email LIKE '%@cern.ch'
  AND cm.created BETWEEN
    '2018-01-01'
    AND (NOW() - INTERVAL '1 month')
