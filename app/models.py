from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime

class NotificationEvent(BaseModel):
    user_id: str
    event_type: str
    message: str
    source: str
    priority_hint: Optional[str] = "low"
    timestamp: datetime
    channel: str
    metadata: Optional[Dict] = {}
    dedupe_key: Optional[str] = None
    expires_at: Optional[datetime] = None