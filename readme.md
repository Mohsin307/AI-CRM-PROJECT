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
