import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Streamlit page title
st.title("🔍 LangChain Chatbot with Search Tools")

# Sidebar for API Key input
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Initialize Arxiv and Wikipedia tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

tools = [arxiv, wiki, search]

# Session state to maintain chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "👋 Hi, I'm a smart search assistant! Ask me anything about research or the web."}
    ]

# Display previous chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input prompt and chatbot logic
if prompt := st.chat_input(placeholder="Ask me something like 'What is LangChain?'") :
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Initialize the LLM
    llm = ChatGroq(
    model="Llama3-8b-8192",
    api_key=api_key,
    streaming=True
)


    # Create the agent
    search_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    # Run the agent and show assistant response
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container())
        response = search_agent.run(prompt, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
