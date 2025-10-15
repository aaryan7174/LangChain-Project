# 🧠 GenAI Search Engine  

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)  
[![LangChain](https://img.shields.io/badge/LangChain-v0.1.0-orange)](https://python.langchain.com/)  
[![Groq](https://img.shields.io/badge/Groq-LLM-green)](https://www.groq.com/)  
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-purple)](https://huggingface.co/)  
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

**An AI-powered semantic search system built using LangChain and Large Language Models (LLMs).**

---

## 🚀 Overview  
The **GenAI Search Engine** transforms the way users explore large document collections.  
Instead of keyword-based retrieval, it delivers **contextual, human-like answers** using embeddings, vector databases, and reasoning-capable LLMs.

---

## ✨ Features  
- 🔍 **Semantic Search:** Retrieves meaning-based results using embeddings.  
- 🗂️ **Smart Chunking:** Efficiently processes and indexes lengthy documents.  
- 💬 **Conversational Responses:** Generates human-like answers using LLMs.  
- ⚙️ **Modular Architecture:** Easy to extend or plug in custom retrievers and models.  
- 🧠 **Context Memory:** Supports multi-turn query understanding.  

---

## 🧰 Tech Stack  
| Category | Technologies |
|-----------|--------------|
| **Language Models** | OpenAI, Hugging Face |
| **Framework** | LangChain |
| **Vector Store** | FAISS / Chroma |
| **Backend** | Python |
| **Interface (Optional)** | Streamlit / Flask |



# GenAI_Search_Engine/
│
├── data/          → Input datasets or document files
├── notebooks/     → Experiments and prototype notebooks
├── src/           → Source code
│   ├── chains/     → LangChain pipeline configurations
│   ├── retrievers/ → Custom retriever logic
│   ├── utils/      → Helper modules
│   └── main.py     → Entry point script
├── requirements.txt → Dependencies
└── README.md        → Documentation






## ⚙️ Setup & Installation  

# 1. Clone the repository
git clone https://github.com/aaryan7174/LangChain-Project.git
cd LangChain-Project/GenAI_Search_Engine

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python src/main.py

Then open your Streamlit or Flask interface to start chatting with your intelligent search engine.

## 🔮 Future Improvements
- Integration with web and API-based data sources
- Multimodal retrieval (text + images)
- LangGraph integration for complex reasoning flows
- Real-time fine-tuning and evaluation dashboard

## 👨‍💻 Author
Aaryan Rana

