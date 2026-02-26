from datetime import datetime

def apply_rules(event):
    score = 0

    if event.priority_hint == "critical":
        score += 80
    elif event.priority_hint == "high":
        score += 50
    elif event.priority_hint == "medium":
        score += 30
    else:
        score += 10

    # Expiry check
    if event.expires_at and event.expires_at < datetime.utcnow():
        return -100  # force NEVER

    return score