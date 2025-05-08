
---

# RAG Multi-Agent Q&A Assistant

A modular, extendable knowledge assistant that uses Retrieval-Augmented Generation (RAG) and multiple specialized tools (calculator, dictionary, retrieval, LLM) for context-aware intelligent answering.  
Built with Python, Streamlit, FAISS, and Groq's LLM.
---
## 🚀 Live Demo

Try out the app here:  
[https://rag-multi-agent-qna-eeeszpxfj2m37hycgsongm.streamlit.app//](https://rag-multi-agent-qna-eeeszpxfj2m37hycgsongm.streamlit.app//)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rag-multi-agent-qna-eeeszpxfj2m37hycgsongm.streamlit.app//)
---

## 🚀 Features

- **RAG pipeline:** Retrieve the most relevant info from your own text docs and ground LLM answers in those.
- **Multi-Agent Router:** Route queries intelligently between calculator, dictionary lookup, or retrieval+LLM.
- **Transparent UI:** Shows agents’ decision path and sources used for answers.
- **Simple deployment:** One-click deploy to [Streamlit Cloud](https://streamlit.io/cloud).
- **Easy extensibility:** Add new tools or sources with minimal code changes.

---

## 🗂️ Project Structure

```
rag-multi-agent-qna/
│
├── app.py               # Streamlit UI + main agent router
├── rag_engine.py        # RAG engine: retrieval & embedding logic
├── tools.py             # Calculator/dictionary utility functions
├── llm.py               # Groq LLM API wrapper
├── docs/                # Plaintext knowledge base documents
│     └── example.txt
├── requirements.txt     # Python dependencies (pinned for compatibility)
├── README.md            # This file
└── .gitignore           # Standard gitignore
```

---

## 🏗️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/RAG-Multi-Agent-QnA.git
cd RAG-Multi-Agent-QnA
```

### 2. Install dependencies (locally)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **Note:** For Streamlit Cloud, all dependencies are auto-installed from `requirements.txt` and `runtime.txt`.

### 3. Add your documents

Place `.txt` files inside the `docs/` folder. Example provided as `docs/example.txt`.

### 4. API Keys

If your Groq LLM requires an API key, store it securely as an environment variable or in [Streamlit secrets management](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management).

---

## 🖥️ Running Locally

```bash
streamlit run app.py
```

Then visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ Deploying on Streamlit Cloud

1. Push your repo to GitHub.
2. Create a new app via [Streamlit Cloud](https://streamlit.io/cloud).
3. Make sure your `runtime.txt` specifies `python-3.10`.
4. Set any required secrets (API keys) in the Streamlit Cloud settings.
5. Click "Deploy".  
6. Use "Clear cache" in the app management menu after major dependency or Python version changes.

---

## 🧩 Usage

- Type any question related to your knowledge base, e.g.:  
  _“What is the onboarding process?”_
- Try agent-based queries:  
  _`calculate 2+2*10`_
  _`define onboarding`_
- The UI displays the decision path and, for RAG answers, the retrieved context.

---

## 🔧 Customization

- **Add new tools:** Add a new function in `tools.py`, extend the `agent_route` logic in `app.py`.
- **Change LLM:** Swap out the LLM wrapper in `llm.py`.
- **Add more documents:** Drop new `.txt` files into `docs/` and redeploy/restart.

---

## ⚠️ Troubleshooting

- **Dependency errors** (e.g., faiss, numpy):  
  All key dependencies are pinned for Python 3.10, NumPy < 2, and compatible huggingface_hub version.
  ```
  # requirements.txt (excerpt)
  torch==2.2.0
  faiss-cpu==1.7.3
  numpy<2
  huggingface_hub<0.16
  sentence-transformers==2.2.2
  streamlit==1.45.0
  ```
  *Do not use Python 3.12 or later—many packages will not have matching binary wheels yet!*

- **Cached_download/huggingface_hub error:**  
  Pin to `huggingface_hub<0.16` as above.

- **NumPy C Extension/ARRAY_API error:**  
  Pin NumPy to `<2`.

---

## 🎯 Roadmap Ideas

- Add more agent skills (e.g., web search, vector DB support).
- Integrate authentication for user-specific data.
- Add caching for faster responses.
- Support for uploading PDF/Word files as knowledge base.

---

## 📝 License

MIT License. See [LICENSE](LICENSE).

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Groq](https://groq.com/) (for LLM interface)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [HuggingFace](https://huggingface.co/)

---

### 💬 For questions, suggestions, or contributions—open an Issue or contact:priyangshu.0718k@gmail.com !

---
