# 🧠 Smart Research Assistant (Offline + Free with Ollama)

A GenAI-powered assistant that reads research documents (PDF/TXT), summarizes them, answers custom questions, and generates logic-based challenges — all **offline** using **open-source models** like `phi3` via Ollama.

## 🚀 Features

- 📄 Upload PDF or TXT documents
- 🧾 Automatic summary (within 100 words)
- ❓ Ask anything (context-aware question answering)
- 🧠 Challenge Me mode (logic-based quiz generation and evaluation)
- 🔌 100% offline using Ollama (`phi3` or other small models)
- 🔍 Justifies each answer with document references

---

## 🏗️ Project Architecture

smart-assistant/
├── backend/ ← FastAPI server
│ ├── app.py ← Main API (summary, ask, challenge, evaluate)
│ └── utils/
│ ├── parser.py ← Handles PDF and TXT parsing
│ ├── summarizer.py ← Summarizes content using Ollama
│ ├── asker.py ← Q&A logic using local LLM + embeddings
│ 
├── frontend/ ← Streamlit UI
│ └── app.py ← User-facing interface
├── README.md


## 🛠️ Setup Instructions

###  1. Install Required Tools

- Python 3.10+: [Download](https://www.python.org/downloads/)
- VS Code (optional): [Download](https://code.visualstudio.com/)
- Ollama: [https://ollama.com](https://ollama.com)

###  2. Pull Lightweight LLM

Use `phi3` (fast and memory-efficient):
bash
ollama run phi3

✅ 4. Install Python Dependencies
pip install requests sentence-transformers pdfplumber fastapi pydantic uvicorn streamlit

✅ 5. Run the Backend (FastAPI)
cd backend
python -m uvicorn app:app --reload --port 7860
You should see:
Uvicorn running on http://127.0.0.1:7860

✅ 6. Run the Frontend (Streamlit)
In a new terminal:
cd frontend
streamlit run app.py
App opens at:
http://localhost:8501



