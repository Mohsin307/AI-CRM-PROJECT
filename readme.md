# 🧠 AI-First CRM HCP Module (LangGraph + Groq + FastAPI + React)

## 🚀 Overview

This project is an **AI-powered CRM system for Healthcare Professionals (HCPs)**.

It allows field representatives to log doctor interactions using:
- Structured form input
- Conversational chat input

The system uses an **AI agent (LangGraph + Groq LLM)** to automatically extract structured CRM insights.

---

## 🎯 Key Features

- 🧠 AI-based interaction summarization
- 📊 Structured CRM data extraction (HCP name, sentiment, product, follow-up)
- 🔄 LangGraph workflow (multi-node AI pipeline)
- 💾 Database storage (SQLite/PostgreSQL)
- 💬 Chat-based interaction logging
- 📋 Interaction history dashboard
- ⚡ Real-time frontend updates

---

## 🏗️ System Architecture

```text
┌──────────────────────────┐
│ React Frontend           │
│ (Chat + Form UI)         │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Redux State Management   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ FastAPI Backend          │
│ REST APIs                │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ LangGraph AI Agent       │
│ Workflow Orchestration   │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Groq LLM                 │
│ gemma2-9b-it             │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ AI Tools Layer           │
│ • Log Interaction Tool   │
│ • Edit Interaction Tool  │
│ • HCP Lookup Tool        │
│ • Product Suggestion Tool│
│ • Follow-up Tool         │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ SQLite / PostgreSQL DB   │
└──────────────────────────┘
```
## Tech Stack

Frontend:
- React
- Redux
- Tailwind CSS

Backend:
- FastAPI
- LangGraph
- Groq API

Database:
- PostgreSQL


##🎯 Features
✅ Structured Interaction Logging

Field representatives can log interactions using forms.

✅ Conversational AI Logging

Users can chat naturally with the AI assistant.

Example:

Visited Dr. Sharma today.
Discussed diabetes medication.
Doctor requested samples next week.

The AI automatically extracts:

Doctor name
Specialty
Products discussed
Follow-up actions
Interaction summary
🤖 LangGraph Agent

The LangGraph agent acts as the intelligent orchestration engine of the CRM system.

Responsibilities:

Understand user input
Maintain workflow state
Decide which tool to execute
Interact with Groq LLM
Process CRM workflows
Store structured outputs

LangGraph enables stateful multi-step AI workflows.

🛠️ LangGraph Tools
1️⃣ Log Interaction Tool

Captures HCP interaction details.

Functions
Summarization
Entity extraction
Sentiment detection
Follow-up identification
Example
Doctor discussed cardiology medicines and requested a demo next Monday.
2️⃣ Edit Interaction Tool

Allows modification of existing interaction records.

Example
Change follow-up date from Monday to Wednesday.
3️⃣ HCP Lookup Tool

Fetches doctor details and interaction history.

Features
Specialty lookup
Previous visits
Prescription trends
Contact information
4️⃣ Product Suggestion Tool

Suggests pharmaceutical products based on doctor specialty and interaction context.

Example
Suggest cardiology-related products.
5️⃣ Follow-Up Reminder Tool

Schedules reminders and tracks pending actions.

Features
Follow-up scheduling
Reminder notifications
Priority tracking
⚙️ Tech Stack
Layer	Technology
Frontend	React + Redux
Backend	FastAPI
AI Workflow	LangGraph
LLM	Groq gemma2-9b-it
Database	PostgreSQL / MySQL
Authentication	JWT
Realtime	WebSockets
Styling	Google Inter Font
