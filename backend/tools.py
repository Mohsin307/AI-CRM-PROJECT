from db import SessionLocal
from models import Interaction

db = SessionLocal()

def log_interaction(data):
    obj = Interaction(**data)
    db.add(obj)
    db.commit()
    return "Logged successfully"

def edit_interaction(id, updates):
    obj = db.query(Interaction).get(id)
    for k, v in updates.items():
        setattr(obj, k, v)
    db.commit()
    return "Updated"

def get_hcp_insights(name):
    data = db.query(Interaction).filter_by(hcp_name=name).all()
    return [d.summary for d in data]

def suggest_next_action(summary):
    return f"Follow-up based on: {summary}"

def summarize_history(name):
    data = db.query(Interaction).filter_by(hcp_name=name).all()
    return " | ".join([d.summary for d in data])