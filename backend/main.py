from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import os
import json
from typing import TypedDict

# ✅ LOAD ENV VARIABLES
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ✅ SAFETY CHECK
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

# ✅ GROQ LLM
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    api_key=GROQ_API_KEY
)

# ✅ LANGGRAPH
from langgraph.graph import StateGraph, END

# ✅ DATABASE
from db import SessionLocal
from models import Interaction

# =========================
# REQUEST MODELS
# =========================
class ChatRequest(BaseModel):
    input: str

class LogRequest(BaseModel):
    hcp_name: str
    summary: str

class InteractionRequest(BaseModel):
    notes: str

# =========================
# FASTAPI APP
# =========================
app = FastAPI(
    title="AI CRM System",
    description="AI-powered CRM to extract structured insights from doctor interactions using LangGraph + Groq",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# LANGGRAPH STATE
# =========================
class State(TypedDict):
    notes: str
    result: dict

# =========================
# AI NODE
# =========================
def extract_data(state: State):
    prompt = f"""
    Extract JSON:
    hcp_name, summary, product, sentiment, follow_up
    
    Text:
    {state['notes']}
"""
    res = llm.invoke(prompt)

    try:
        data = json.loads(res.content)
    except:
        data = {
            "hcp_name": "Unknown",
            "summary": state["notes"],
            "product": "Unknown",
            "sentiment": "Neutral",
            "follow_up": "Review later"
        }

    return {"result": data}

# =========================
# DB NODE
# =========================
def save_to_db(state: State):
    db = SessionLocal()

    obj = Interaction(**state["result"])
    db.add(obj)
    db.commit()

    return state

# =========================
# LANGGRAPH WORKFLOW
# =========================
graph = StateGraph(State)

graph.add_node("extract", extract_data)
graph.add_node("save", save_to_db)

graph.set_entry_point("extract")
graph.add_edge("extract", "save")
graph.add_edge("save", END)

workflow = graph.compile()

# =========================
# ROUTES
# =========================

@app.get("/")
def home():
    return {"msg": "Backend working perfectly"}

# -------- CHAT API --------
@app.post("/chat")
def chat(data: ChatRequest):
    return {"response": f"You said: {data.input}"}

# -------- MANUAL LOG --------
@app.post("/log")
def log(data: LogRequest):
    return {
        "msg": "Saved successfully",
        "data": {
            "hcp_name": data.hcp_name,
            "summary": data.summary
        }
    }

# -------- AI LOG (LangGraph) --------
@app.post("/log-ai")
def log_ai(data: InteractionRequest):

    result = workflow.invoke({
        "notes": data.notes
    })

    return {
    "status": "success",
    "interaction": result["result"]
}

# -------- GET INTERACTIONS --------
@app.get("/interactions")
def get_interactions():
    db = SessionLocal()
    data = db.query(Interaction).all()

    return [
        {
            "id": i.id,
            "hcp_name": i.hcp_name,
            "summary": i.summary,
            "product": i.product,
            "sentiment": i.sentiment,
            "follow_up": i.follow_up,
        }
        for i in data
    ]