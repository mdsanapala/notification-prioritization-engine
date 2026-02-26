from datetime import datetime
import uuid

from app.rule_engine import apply_rules
from app.dedupe import check_duplicate
from app.fatigue import calculate_fatigue
from app.ai_scorer import get_ai_score
from app.database import SessionLocal
from app.audit import AuditLog


def process_notification(event):

    db = SessionLocal()
    event_id = str(uuid.uuid4())

    decision = None
    reason = None
    explanation = {}

    # 1️⃣ Expiry Check
    if event.expires_at and event.expires_at < datetime.utcnow():
        decision = "NEVER"
        reason = "Expired notification"

    # 2️⃣ Hard Override Rule (Critical always NOW)
    elif event.priority_hint == "critical":
        decision = "NOW"
        reason = "Critical priority override"

    # 3️⃣ Deduplication (TTL-based)
    elif check_duplicate(event):
        decision = "NEVER"
        reason = "Duplicate within 5-minute window"

    else:
        # 4️⃣ Rule Score
        rule_score = apply_rules(event)

        # 5️⃣ Fatigue
        fatigue_penalty = calculate_fatigue(event)

        # 6️⃣ AI Score
        ai_score = get_ai_score(event)

        # 7️⃣ Final Score
        final_score = rule_score + ai_score - fatigue_penalty

        explanation = {
            "rule_score": rule_score,
            "ai_score": ai_score,
            "fatigue_penalty": fatigue_penalty,
            "final_score": final_score
        }

        # 8️⃣ Classification
        if final_score > 75:
            decision = "NOW"
        elif final_score > 40:
            decision = "LATER"
        else:
            decision = "NEVER"

        reason = "Scored decision"

    # 🔥 Persist Audit Log
    audit_entry = AuditLog(
        event_id=event_id,
        user_id=event.user_id,
        decision=decision,
        reason=reason,
        explanation=explanation
    )

    db.add(audit_entry)
    db.commit()
    db.close()

    return {
        "event_id": event_id,
        "decision": decision,
        "reason": reason,
        "explanation": explanation
    }