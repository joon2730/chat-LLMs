import streamlit as st
import time

from chat_llms.llm import ChatLLM

# buffer for delayed response
user_message_buffer = list()

# App title
st.set_page_config(page_title="ChatLLM", page_icon="☕", layout="wide")

# Initialize session state
if "messages" not in st.session_state.keys():
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def reply_to_message(user_message="*silence*"):
    # Check if model is initialized
    if "model" in st.session_state.keys():
        # model response
        with st.chat_message("assistant"): 
            with st.spinner("..."):
                placeholder = st.empty()
                full_response = ''
                for item in st.session_state.model.generate_response(user_message):
                    full_response += item
                    placeholder.markdown(full_response)
        # Save assistant message
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Get user input
if prompt := st.chat_input("Send a message"):
    st.session_state.messages.append({"role": "user", "content": prompt}) # Save user message
    with st.chat_message("user"):
        st.markdown(prompt)     # Display user message

    # model response
    reply_to_message(prompt)
    
# Initialize model
if "model" not in st.session_state.keys():
    st.session_state.model = ChatLLM()
    reply_to_message()

