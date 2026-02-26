ALTER TABLE fact_logs CLUSTER BY (TO_DATE(event_time), severity, event_type);

ALTER TABLE fact_logs ADD SEARCH OPTIMIZATION ON EQUALITY(user_id, event_type, severity);

CREATE OR REPLACE MATERIALIZED VIEW mv_daily_severity AS
SELECT TO_DATE(event_time) AS event_date, severity, COUNT(*) AS cnt
FROM fact_logs
GROUP BY 1, 2;
