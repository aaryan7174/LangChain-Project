import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Optional: LangSmith Tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "Langchain_Ollama_App")

# -------------------- Streamlit Config --------------------
st.set_page_config(
    page_title="🤖 Langchain x Ollama | AI Assistant",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
    <style>
    .big-title {
        font-size: 60px;
        font-weight: bold;
        color: #4B8BBE;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }
    .stTextInput > label {
        font-size: 20px !important;
    }
    .stButton > button {
        font-size: 18px !important;
        padding: 0.5em 2em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🧠 Langchain + Ollama Chat Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything. Explore everything. Powered by `gemma2:2b` or your custom model.</div>', unsafe_allow_html=True)

# -------------------- Sidebar Controls --------------------
with st.sidebar:
    st.header("⚙️ LLM Configuration", divider="rainbow")
    model_name = st.text_input("Model Name", value="gemma2:2b")
    temperature = st.slider("🎚 Temperature", 0.0, 1.5, 0.7, step=0.1)
    top_p = st.slider("🎯 Top-p", 0.0, 1.0, 0.9, step=0.05)
    repeat_penalty = st.slider("🔁 Repeat Penalty", 0.5, 2.0, 1.0, step=0.1)

# -------------------- Langchain Setup --------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}")
])

llm = Ollama(
    model=model_name,
    temperature=temperature,
    top_p=top_p,
    repeat_penalty=repeat_penalty
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# -------------------- Main Input & Output --------------------
st.markdown("### 💬 Ask Your Question Below")
input_question = st.text_input("Type your query here:")

if input_question:
    with st.spinner("✨ Thinking really hard..."):
        response = chain.invoke({"question": input_question})
        st.markdown("### ✅ **AI Response**")
        st.markdown(f"""
        <div style="background-color: #f1f3f5; padding: 20px; border-radius: 10px; font-size: 18px;">
            {response}
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📋 LLM Configuration Used"):
            st.write(f"**Model:** {model_name}")
            st.write(f"**Temperature:** {temperature}")
            st.write(f"**Top-p:** {top_p}")
            st.write(f"**Repeat Penalty:** {repeat_penalty}")

# -------------------- Footer --------------------
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>Made with ❤️ using Langchain & Ollama | Streamlit Magic ✨</div>",
    unsafe_allow_html=True
)
