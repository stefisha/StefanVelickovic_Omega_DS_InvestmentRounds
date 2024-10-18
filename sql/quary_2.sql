WITH transaction_streaks AS (
  SELECT 
    user_id, 
    transaction_category,
    is_successful,
    created_at,
    ROW_NUMBER() OVER (PARTITION BY user_id, transaction_category ORDER BY created_at) 
        - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at) AS streak_id
  FROM transactions
  WHERE is_successful = 'yes'
)
SELECT user_id, transaction_category, COUNT(*) AS streak_length
FROM transaction_streaks
GROUP BY user_id, transaction_category, streak_id
HAVING COUNT(*) >= 4;