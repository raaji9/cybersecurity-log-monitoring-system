from datetime import datetime, timezone
from ipaddress import ip_address
from typing import Any, Dict, List, Optional

VALID_SEVERITIES = {"LOW", "MEDIUM", "HIGH", "CRITICAL"}

def _safe_ip(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    try:
        return str(ip_address(value))
    except ValueError:
        return None

def _safe_ts(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt.astimezone(timezone.utc).isoformat()
    except ValueError:
        return None

def transform_logs(logs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    transformed = []
    for log in logs:
        sev = str(log.get("severity", "LOW")).upper()
        transformed.append({
            "user_id": log.get("user_id"),
            "event_time": _safe_ts(log.get("timestamp")),
            "event_type": log.get("event"),
            "severity": sev if sev in VALID_SEVERITIES else "LOW",
            "source_ip": _safe_ip(log.get("src_ip")),
            "destination_ip": _safe_ip(log.get("dst_ip")),
        })
    return transformed
