from datetime import datetime, timedelta

def get_burst_count(history, uid, lookback_mins=15):
    # simple count for rapid fire attempts
    cutoff = datetime.now() - timedelta(minutes=lookback_mins)
    c = 0
    for item in history:
        if item.get("uid") == uid:
            ts = item.get("ts")
            if isinstance(ts, str):
                try:
                    ts = datetime.fromisoformat(ts)
                except Exception:
                    continue
            if ts and ts >= cutoff:
                c += 1
    return c
