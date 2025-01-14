from checks.velocity import get_burst_count
from checks.fingerprints import find_linked_accounts

def evaluate_risk(order, user_meta, history_rows, account_pool):
    score = 0
    flags = []
    
    uid = order.get("uid")
    amount = order.get("amount", 0)
    
    # 1. velocity check
    burst = get_burst_count(history_rows, uid, lookback_mins=15)
    if burst >= 4:
        score += 45
        flags.append(f"velocity_spike ({burst} in 15m)")
    elif burst >= 2:
        score += 15
        
    # 2. alt account detection
    alts = find_linked_accounts(account_pool, uid)
    if alts:
        score += 35
        flags.append(f"shared_identity_with_{len(alts)}_alts")
        
    # 3. fresh account with relatively high amount
    account_age = user_meta.get("days_since_reg", 999)
    if account_age < 2 and amount > 100:
        score += 25
        flags.append("new_account_high_ticket")
        
    # 4. failed payment streak
    if user_meta.get("failed_payment_streak", 0) >= 3:
        score += 30
        flags.append("failed_payment_streak")
        
    if score >= 75:
        action = "REJECT_OR_HOLD"
    elif score >= 45:
        action = "MANUAL_REVIEW"
    else:
        action = "PASS"
        
    return {
        "uid": uid,
        "score": score,
        "action": action,
        "flags": flags
    }
