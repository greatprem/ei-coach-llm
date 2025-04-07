import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Page Config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Header
st.title("🧠 Emotional Intelligence Chatbot")
st.write("Ask anything related to self-awareness, leadership, or emotional intelligence.")

# API Setup
api_key = os.getenv("OPENROUTER_API_KEY")
model = "meta-llama/llama-4-maverick"  # Switch to any available model

# Chat input
user_input = st.text_input("🗣️ You:", placeholder="Type your question here...")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.markdown(f"**You:** {msg['user']}")
    st.markdown(f"**AI:** {msg['ai']}")

# Send to OpenRouter on submit
if user_input:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": user_input}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        content = response.json()["choices"][0]["message"]["content"]
        st.session_state.messages.append({"user": user_input, "ai": content})
        st.experimental_rerun()  # Refresh to show updated chat
    except Exception as e:
        st.error("Something went wrong. Try again or check your model/API key.")
        st.text(response.text)