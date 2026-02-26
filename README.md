📢 Notification Prioritization Engine

An intelligent backend system that classifies incoming notifications into:

✅ NOW

⏳ LATER

❌ NEVER

The system reduces notification overload using:

Hard override rules

TTL-based deduplication

Alert fatigue control

AI-assisted scoring

Full audit logging

Explainable decision outputs

🚀 Problem Statement

Users receive too many notifications.
Some are repetitive.
Some arrive at bad times.
Some low-value notifications are sent while important ones are delayed.

This system ensures:

Important notifications are prioritized.

Duplicates are suppressed.

Alert fatigue is reduced.

Every decision is explainable and auditable.

🏗 Architecture Overview
1️⃣ Input Layer

Receives notification events via FastAPI endpoint:

POST /notifications
2️⃣ Decision Engine Pipeline

Expiry Check

Critical Override

Duplicate Detection (TTL window)

Rule-Based Scoring

Fatigue Penalty

AI Score

Final Classification (NOW / LATER / NEVER)

🧠 Decision Strategy
Hard Rules

Expired → NEVER

Critical → NOW

Deduplication

Suppresses duplicate notifications within 5-minute window.

Alert Fatigue

Applies penalty after threshold per user.

Scoring
Final Score = Rule Score + AI Score - Fatigue Penalty
Score Range	Decision
> 75	NOW
40–75	LATER
< 40	NEVER
🗄 Audit & Explainability

Each event:

Generates UUID event_id

Stores decision in SQLite

Logs explanation object

Can be retrieved via:

GET /audit/{event_id}
📦 Tech Stack

Python

FastAPI

SQLAlchemy

SQLite

Pydantic

(Optional) Redis

(Optional) APScheduler

(Optional) scikit-learn

🧪 Example Request
{
  "user_id": "u123",
  "event_type": "alert",
  "message": "Server Down!",
  "source": "system",
  "priority_hint": "critical",
  "timestamp": "2026-02-26T10:00:00",
  "channel": "push"
}
Example Response
{
  "event_id": "uuid",
  "decision": "NOW",
  "reason": "Critical priority override",
  "explanation": {}
}
🔍 Health Check
GET /health

Returns:

{
  "status": "Notification Engine Running"
}
🎯 Features Implemented

 NOW / LATER / NEVER classification

 TTL-based duplicate suppression

 Alert fatigue protection

 Explainable scoring logic

 Persistent audit logging

 UUID tracking

 Modular architecture

📈 Future Improvements

Redis-based distributed dedupe

Background scheduler for LATER

ML-based scoring model

Metrics & monitoring

Dynamic rule configuration

🧠 Design Philosophy

This system prioritizes:

Reliability

Explainability

Auditability

Scalability

Clear separation of concerns

💡 Author

Murali Dharan Sanapala
AI/ML & Backend Engineering Enthusiast
