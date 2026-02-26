from datetime import datetime, timedelta

# Store {key: timestamp}
recent_messages = {}

# 5 minute dedupe window
DEDUP_WINDOW = timedelta(minutes=5)

def check_duplicate(event):

    key = f"{event.user_id}-{event.message}"
    now = datetime.utcnow()

    # Clean expired entries
    keys_to_delete = []
    for k, timestamp in recent_messages.items():
        if now - timestamp > DEDUP_WINDOW:
            keys_to_delete.append(k)

    for k in keys_to_delete:
        del recent_messages[k]

    # Check duplicate
    if key in recent_messages:
        return True

    # Store new entry
    recent_messages[key] = now
    return False