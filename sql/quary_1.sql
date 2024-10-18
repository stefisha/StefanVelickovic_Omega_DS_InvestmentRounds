SELECT user_id, COUNT(*) as transaction_count
FROM transactions
WHERE YEAR(created_at) = '2022'
	AND membership = 'free'
GROUP BY user_id;