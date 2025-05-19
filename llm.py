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
    system_prompt = (
        "You are a precise and reliable AI assistant tasked with answering questions strictly based on the given context.\n"
        "Do NOT use prior knowledge or make assumptions beyond the context.\n"
        "If the answer is not explicitly stated or inferable from the context, respond with:\n"
        "'I'm sorry, the information is not available in the provided context.'\n"
        "Always prioritize factual accuracy, clarity, and transparency in your responses."
    )

    user_prompt = (
        "------------------------\n"
        f"Context:\n{context}\n"
        "------------------------\n"
        f"Question: {question}\n"
        "Answer:"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "max_tokens": 512,
        "temperature": 0.2
    }
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
