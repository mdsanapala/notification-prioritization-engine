from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.models import NotificationEvent
from app.decision_engine import process_notification
from app.database import engine, Base, SessionLocal
from app.audit import AuditLog


# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notification Prioritization Engine")


# 🔹 Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Submit Notification
@app.post("/notifications")
def receive_notification(event: NotificationEvent):
    return process_notification(event)


# 🔹 Fetch Audit Log
@app.get("/audit/{event_id}")
def get_audit(event_id: str, db: Session = Depends(get_db)):

    record = db.query(AuditLog).filter(AuditLog.event_id == event_id).first()

    if not record:
        return {"error": "Event not found"}

    return {
        "event_id": record.event_id,
        "user_id": record.user_id,
        "decision": record.decision,
        "reason": record.reason,
        "explanation": record.explanation,
        "created_at": record.created_at
    }


# 🔹 Health Check Endpoint
@app.get("/health")
def health_check():
    return {"status": "Notification Engine Running"}