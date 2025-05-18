import os
os.environ['STREAMLIT_WATCHER_TYPE'] = 'none'
import streamlit as st
st.set_page_config(page_title="RAG Multi-Agent Q&A", layout="centered")

import glob
from rag_engine import RAGEngine
from tools import calculator, dictionary_lookup
from llm import groq_chat_completion
st.title("📚 RAG Multi-Agent Q&A Assistant")
st.write("Upload multiple documents and ask questions! Supports PDF, DOCX, TXT.")

DOCS_FOLDER = "docs"
os.makedirs(DOCS_FOLDER, exist_ok=True)


# Upload section
uploaded_files = st.file_uploader("Upload documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)

# Save uploaded files to docs folder
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(DOCS_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.success(f"{len(uploaded_files)} document(s) saved in `{DOCS_FOLDER}/`.")

# Initialize RAG engine with docs folder
try:
    rag = RAGEngine(docs_folder=DOCS_FOLDER)
except Exception as e:
    st.error(f"Error initializing RAGEngine: {e}")
    st.stop()

query = st.text_input("Ask your question:")

if query:
    log = []
    query_l = query.lower().strip()

    if query_l.startswith("calculate"):
        log.append("Decision: Calculator")
        result = calculator(query_l[len("calculate"):].strip())
        st.success(result)

    elif query_l.startswith("define"):
        log.append("Decision: Dictionary")
        result = dictionary_lookup(query_l[len("define"):].strip())
        st.success(result)

    else:
        log.append("Decision: RAG Retrieval")
        ctx = rag.retrieve(query)
        context_block = '\n---\n'.join([f"[{src}] {chunk}" for chunk, src in ctx])
        prompt = f"Context:\n{context_block}\n\nQuestion: {query}\nAnswer:"
        answer = groq_chat_completion(prompt)

        with st.expander("Retrieved Context"):
            for chunk, src in ctx:
                st.markdown(f"- **{src}**: {chunk}")

        st.subheader("Answer")
        st.write(answer)

    with st.expander("Decision Log"):
        for l in log:
            st.text(l)

