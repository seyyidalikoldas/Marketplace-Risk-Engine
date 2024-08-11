def find_linked_accounts(dataset, target_uid):
    matches = set()
    target_ip = None
    target_fp = None
    
    for row in dataset:
        if row.get("uid") == target_uid:
            target_ip = row.get("ip")
            target_fp = row.get("hw_id")
            break
            
    if not target_ip and not target_fp:
        return []
        
    for row in dataset:
        curr_uid = row.get("uid")
        if curr_uid == target_uid:
            continue
        # check shared ip or device hash
        if target_ip and row.get("ip") == target_ip:
            matches.add(curr_uid)
        elif target_fp and row.get("hw_id") == target_fp:
            matches.add(curr_uid)
            
    return list(matches)
