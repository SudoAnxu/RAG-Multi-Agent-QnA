import os
import requests
import streamlit as st
GROQ_API_KEY =  st.secrets["GROQ_API_KEY"] #or os.getenv("GROQ_API_KEY") 
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Set it in your environment or Streamlit secrets.")
GROQ_MODEL = "llama3-70b-8192"  

def groq_chat_completion(prompt):
    url = 'https://api.groq.com/openai/v1/chat/completions'
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use the provided context if available."},
        {"role": "user", "content": prompt}
    ]
    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "max_tokens": 256,
        "temperature": 0.2
    }
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    if r.status_code == 200:
        return r.json()["choices"][0]["message"]["content"].strip()
    else:
        return f"LLM Error: {r.text}"