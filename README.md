📢 Notification Prioritization Engine

An intelligent, explainable backend system that classifies incoming notification events into:

<<<<<<< HEAD
=======

>>>>>>> 2eaae1ffaab493acbfca0df753560b227e9fc89d
✅ NOW (send immediately)

⏳ LATER (deferred / scheduled)

❌ NEVER (suppressed)

The system reduces notification overload using:

Hard override rules

TTL-based duplicate suppression

Alert fatigue control

AI-assisted scoring

Persistent audit logging

Explainable decision outputs

🚀 Problem Statement

Modern applications send notifications from multiple sources (messages, alerts, promotions, system events). Users often experience:

Too many notifications

Duplicate messages

Low-value spam

Important alerts being delayed

Notification fatigue

This engine ensures:

Important notifications are prioritized

Duplicates are suppressed

Alert fatigue is minimized

Every decision is explainable and auditable

The system fails safely under dependency issues

🏗 High-Level Architecture
<<<<<<< HEAD
=======

>>>>>>> 2eaae1ffaab493acbfca0df753560b227e9fc89d
Incoming Event
      │
      ▼
API Layer (FastAPI)
      │
      ▼
Decision Engine
 ├── Expiry Check
 ├── Critical Override
 ├── Deduplication (TTL)
 ├── Rule-Based Scoring
 ├── Fatigue Penalty
 ├── AI Score
      │
      ▼
Final Classification
(NOW / LATER / NEVER)
      │
      ▼
Audit Log (SQLite)
🧠 Decision Logic Strategy

The decision pipeline follows this strict order:

1️⃣ Expiry Check

If expires_at < current_time → NEVER

2️⃣ Critical Override

If priority_hint == critical → NOW

3️⃣ Duplicate Suppression

TTL-based (5 minutes) suppression using:

dedupe:{user_id}:{message}

If duplicate → NEVER

4️⃣ Scoring System
Final Score = Rule Score + AI Score - Fatigue Penalty
Score Range	Decision
> 75	NOW
40–75	LATER
< 40	NEVER
🧾 API Interfaces (5 Endpoints)
1️⃣ POST /notifications

Main decision endpoint.

Request
{
  "user_id": "u123",
  "event_type": "alert",
  "message": "Server Down!",
  "source": "system",
  "priority_hint": "critical",
  "timestamp": "2026-02-26T10:00:00",
  "channel": "push"
}
Response
{
  "event_id": "uuid",
  "decision": "NOW",
  "reason": "Critical priority override",
  "explanation": {}
}
2️⃣ GET /audit/{event_id}

Retrieve stored decision for transparency.

3️⃣ GET /health

Health check endpoint.

4️⃣ GET /metrics

Returns decision distribution & monitoring statistics.

5️⃣ POST /rules/update

Supports dynamic rule configuration without redeployment.

🗄 Data Model
NotificationEvent

user_id

event_type

message

source

priority_hint

timestamp

channel

expires_at (optional)

AuditLog

event_id (UUID)

user_id

decision

reason

explanation (JSON)

created_at

🔁 Duplicate Prevention Strategy

Uses 5-minute TTL window

Suppresses repeated notifications

Prevents spam bursts

Designed to scale with Redis (future upgrade)

🔔 Alert Fatigue Strategy

Tracks per-user notification count

Applies penalty after threshold

Reduces noisy, low-priority events

Protects user experience

🧠 AI Scoring Layer

AI scoring component evaluates likelihood of engagement

Combined with rule score

Designed to fallback safely if AI service fails

🛡 Fail-Safe Strategy

If any dependent component fails:

AI failure → fallback to rule score

DB failure → decision still returned, error logged

Redis failure → fallback to in-memory dedupe

System always returns a decision (no silent drops)

📊 Monitoring & Metrics Plan

System designed to support:

Decision distribution tracking

Duplicate rate monitoring

Fatigue-trigger frequency

Latency monitoring

Error rate tracking

⚙️ Tech Stack

Python

FastAPI

SQLAlchemy

SQLite

Pydantic

Redis (scalable dedupe)

APScheduler (optional scheduling)

scikit-learn (AI scoring)

🚀 Running Locally
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Run server
uvicorn app.main:app --reload
3️⃣ Access docs
http://127.0.0.1:8000/docs
📈 Future Improvements

Redis cluster support

Distributed deployment

Background worker for LATER queue

Real-time push integration

ML model training dashboard

Rate-limiting per channel

User preference learning

🎯 Design Principles

Explainability first

Deterministic decision order

Modular architecture

Extensible scoring system

Audit-compliant logging

Scalability-ready design

👨‍💻 Author

Murali Dharan Sanapala
AI/ML & Backend Engineering Enthusiast

🏁 Summary


