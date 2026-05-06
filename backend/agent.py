from groq import Groq
from tools import *

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")



def ask_llm(prompt):
    res = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content


def run_agent(user_input):
    if "edit" in user_input:
        return edit_interaction(1, {"summary": "updated via AI"})
    
    elif "history" in user_input:
        return summarize_history("Dr Rao")
    
    else:
        return ask_llm(f"Convert this into structured CRM JSON: {user_input}")