import os
import snowflake.connector
from snowflake.connector import DictCursor
from typing import Dict, List, Any

INSERT_SQL = """
INSERT INTO fact_logs (user_id, event_time, event_type, severity, source_ip, destination_ip)
VALUES (%(user_id)s, %(event_time)s, %(event_type)s, %(severity)s, %(source_ip)s, %(destination_ip)s)
"""

def load_to_snowflake(transformed_logs: List[Dict[str, Any]]) -> int:
    if not transformed_logs:
        return 0

    conn = snowflake.connector.connect(
        user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"],
        account=os.environ["SNOWFLAKE_ACCOUNT"],
        warehouse=os.environ.get("SNOWFLAKE_WAREHOUSE", "COMPUTE_WH"),
        database=os.environ.get("SNOWFLAKE_DATABASE", "CYBERSECURITY_DB"),
        schema=os.environ.get("SNOWFLAKE_SCHEMA", "PUBLIC"),
        role=os.environ.get("SNOWFLAKE_ROLE", "SECURITY_INGESTOR"),
    )
    try:
        with conn.cursor(DictCursor) as cur:
            cur.executemany(INSERT_SQL, transformed_logs)
        conn.commit()
        return len(transformed_logs)
    finally:
        conn.close()
