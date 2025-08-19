# marketplace-risk-engine

Collection of Python checks and SQL queries I use to detect fraudulent transaction spikes, multi-account abuse, and compromised accounts across marketplace transactions and Discord moderation queues.

### what it does:
- `checks/velocity.py`: flags rapid transaction bursts within 15-min windows.
- `checks/fingerprints.py`: detects account linkage using shared IP address or hardware fingerprint hashes.
- `evaluator.py`: weighs signals (account age, failed card streaks, velocity, alt count) to categorize into PASS / MANUAL_REVIEW / REJECT.
- `sql/fraud_investigation.sql`: queries for finding IP collision clusters with chargeback history.

### run test:
```bash
python run.py
```
