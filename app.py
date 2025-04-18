import streamlit as st
import time
import uuid
from chat_llms.loader import get_model

# App title
st.set_page_config(page_title="ChatLLM", page_icon="☕", layout="wide")

# Initialize session state
if "messages" not in st.session_state.keys():
    st.session_state.messages = []
if "session_id" not in st.session_state.keys():
    st.session_state.session_id = str(uuid.uuid4())
if "model" not in st.session_state.keys():
    st.session_state.model = get_model()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def reply_to_message(user_message="*user entered chat*"):
    # model response
    with st.chat_message("assistant"): 
        with st.spinner("..."):
            placeholder = st.empty()
            session_id = st.session_state.session_id
            response = st.session_state.model.generate_response(user_message, session_id)
            placeholder.markdown(response)

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})

# Get user input
if prompt := st.chat_input("Send a message"):
    st.session_state.messages.append({"role": "user", "content": prompt}) # Save user message
    with st.chat_message("user"):
        st.markdown(prompt)     # Display user message

    # model response
    reply_to_message(prompt)
    

