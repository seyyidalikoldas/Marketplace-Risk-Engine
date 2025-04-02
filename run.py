from datetime import datetime
from evaluator import evaluate_risk

def main():
    # test dummy data
    test_user = {"days_since_reg": 1, "failed_payment_streak": 3}
    test_order = {"uid": "usr_test_901", "amount": 160.0}
    
    sample_history = [
        {"uid": "usr_test_901", "ts": datetime.now()},
        {"uid": "usr_test_901", "ts": datetime.now()},
        {"uid": "usr_test_901", "ts": datetime.now()},
        {"uid": "usr_test_901", "ts": datetime.now()}
    ]
    
    sample_accounts = [
        {"uid": "usr_test_901", "ip": "178.23.4.1", "hw_id": "hw_f8a92"},
        {"uid": "usr_banned_12", "ip": "178.23.4.1", "hw_id": "hw_f8a92"}
    ]
    
    res = evaluate_risk(test_order, test_user, sample_history, sample_accounts)
    print("Evaluation result:", res)

if __name__ == "__main__":
    main()
