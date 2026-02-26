user_counts = {}

def calculate_fatigue(event):
    user = event.user_id

    if user not in user_counts:
        user_counts[user] = 0

    user_counts[user] += 1

    # Simple fatigue rule
    if user_counts[user] > 5:
        return 30  # fatigue penalty

    return 0