🧠 Conversation QnA Chatbot
An intelligent RAG (Retrieval-Augmented Generation)-based conversational chatbot built using LangChain, Groq LLM, and Hugging Face Embeddings.
It can fetch live data from the web, store vector embeddings, and answer user queries contextually — maintaining chat history awareness for natural, continuous dialogue.

🚀 Project Overview
This chatbot demonstrates how to integrate:

LangChain’s RAG Pipeline (Retriever + LLM)

Groq LLM (llama3-8b-8192)

Hugging Face Sentence Transformer Embeddings

Chroma Vector Store

Contextual Question Answering with Chat History

The system dynamically retrieves information from an online source, splits it into chunks, stores embeddings in a vector database, and generates accurate, context-aware responses.

⚙️ Tech Stack
Component

Description

LangChain

Framework for building LLM-powered applications

Groq API

High-performance inference for llama3-8b-8192

Hugging Face

Embeddings model (all-MiniLM-L6-v2)

Chroma DB

Vector database for semantic search

BeautifulSoup4

Web content extraction

Dotenv

Environment variable management

🧩 Project Workflow
flowchart TD
    A[Load .env Variables] --> B[Initialize Groq LLM]
    B --> C[Load Web Documents using WebBaseLoader]
    C --> D[Split Documents with RecursiveCharacterTextSplitter]
    D --> E[Generate Embeddings using HuggingFace Model]
    E --> F[Store Embeddings in Chroma Vector DB]
    F --> G[Retriever Fetches Context]
    G --> H[LLM Generates Context-Aware Answers]
    H --> I[Maintains Chat History for Follow-ups]

✅ Core Features
RAG Implementation – Combines retrieval with generation for precise, fact-based answers.

Chat History Awareness – Understands conversation flow and context continuity.

Dynamic Web Data Loading – Fetches live content using WebBaseLoader.

Multi-Turn Dialogue Support – Maintains user sessions for ongoing chats.

Lightweight & Fast – Optimized with Groq LLM for low-latency inference.

🧰 Installation
Clone the repository and navigate to the folder:

git clone [https://github.com/aaryan7174/LangChain-Project.git](https://github.com/aaryan7174/LangChain-Project.git)
cd LangChain-Project/4-Conversation_QnA_Chatbot

Create a virtual environment:

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
# python -m venv venv
# venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

🔑 Environment Variables
Create a .env file in the project root with the following keys:

GROQ_API_KEY="your_groq_api_key"
HF_TOKEN="your_huggingface_token"

🧠 Usage
Run the notebook or script:

jupyter notebook Conversation_QnA_Chatbot.ipynb

Example Interaction:
User: What is an AI agent?
Bot: An AI agent is a system that uses a Large Language Model (LLM) as its core controller, capable of planning, reflecting, and refining its actions to improve performance over time.

User: Tell me more about it.
Bot: It’s powered by an LLM acting as the “brain,” supported by memory and planning modules to execute complex tasks autonomously.

📂 Project Structure
LangChain-Project/
│
└─── 4-Conversation_QnA_Chatbot/
     ├── Conversation_QnA_Chatbot.ipynb
     ├── requirements.txt
     ├── .env
     └── README.md

📖 References
LangChain Documentation

Groq Cloud API

Hugging Face Sentence Transformers

Lilian Weng Blog Post

👨‍💻 Author
Aaryan Rana
