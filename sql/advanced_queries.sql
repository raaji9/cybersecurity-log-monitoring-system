WITH high_severity AS (
  SELECT user_id, COUNT(*) AS event_count
  FROM fact_logs
  WHERE severity IN ('HIGH', 'CRITICAL')
  GROUP BY user_id
)
SELECT u.username, h.event_count
FROM high_severity h
JOIN dim_users u ON h.user_id = u.user_id
ORDER BY h.event_count DESC;

SELECT
  user_id,
  event_time,
  COUNT(*) OVER (
    PARTITION BY user_id
    ORDER BY event_time
    RANGE BETWEEN INTERVAL '1 hour' PRECEDING AND CURRENT ROW
  ) AS events_last_hour
FROM fact_logs;
