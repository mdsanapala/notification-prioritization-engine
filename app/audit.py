from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from app.database import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String, index=True)
    user_id = Column(String)
    decision = Column(String)
    reason = Column(String)
    explanation = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)