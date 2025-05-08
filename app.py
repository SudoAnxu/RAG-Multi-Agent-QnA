import streamlit as st
st.set_page_config(page_title="RAG Multi-Agent Q&A", layout="centered")

from rag_engine import RAGEngine
from tools import calculator, dictionary_lookup
from llm import groq_chat_completion

DOCS_FOLDER = "docs"

# Instantiate RAG pipeline
@st.cache_resource(show_spinner="Embedding docs and building index ...")
def load_rag():
    return RAGEngine(DOCS_FOLDER)

rag = load_rag()

def agent_route(query):
    log = []
    query_l = query.lower().strip()
    if query_l.startswith("calculate"):
        expr = query_l[len("calculate"):].strip()
        log.append("Decision: Routed to CALCULATOR tool")
        result = calculator(expr)
        return log, None, result
    elif query_l.startswith("define"):
        word = query_l[len("define"):].strip()
        log.append("Decision: Routed to DICTIONARY tool")
        result = dictionary_lookup(word)
        return log, None, result
    else:
        log.append("Decision: Routed to RAG (Retrieve + LLM)")
        ctx = rag.retrieve(query)
        context_block = '\n---\n'.join([f"[{src}] {chunk}" for chunk, src in ctx])
        llm_prompt = f"Context:\n{context_block}\n\nQuestion: {query}\nAnswer:"
        answer = groq_chat_completion(llm_prompt)
        return log, ctx, answer

# UI
st.title("RAG Multi-Agent Q&A Assistant")
st.write("Ask about the knowledge base, or try e.g. `calculate 2+2*10`, or `define onboarding`.")

query = st.text_input("Your question:")

if query:
    log, ctx, answer = agent_route(query)
    with st.expander("Decision Log"):
        for step in log:
            st.write(step)
    if ctx:
        with st.expander("Retrieved Context"):
            for chunk, src in ctx:
                st.markdown(f"- **{src}**: {chunk}")
    st.subheader("Final Answer")
    st.write(answer)
