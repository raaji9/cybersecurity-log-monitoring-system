CREATE OR REPLACE TABLE dim_users (
  user_id NUMBER PRIMARY KEY,
  username STRING NOT NULL,
  department STRING
);

CREATE OR REPLACE TABLE dim_event_types (
  event_type STRING PRIMARY KEY,
  description STRING
);

CREATE OR REPLACE TABLE fact_logs (
  log_id NUMBER AUTOINCREMENT PRIMARY KEY,
  user_id NUMBER NOT NULL,
  event_time TIMESTAMP_NTZ NOT NULL,
  event_type STRING NOT NULL,
  severity STRING NOT NULL,
  source_ip STRING,
  destination_ip STRING,
  CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES dim_users(user_id),
  CONSTRAINT fk_event_type FOREIGN KEY (event_type) REFERENCES dim_event_types(event_type),
  CONSTRAINT chk_severity CHECK (severity IN ('LOW','MEDIUM','HIGH','CRITICAL'))
)
CLUSTER BY (TO_DATE(event_time), severity);
