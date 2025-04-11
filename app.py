import streamlit as st
import time

from chat_llms.llm import ChatLLM

# App title
st.set_page_config(page_title="ChatLLM", page_icon="☕", layout="wide")

# Initialize session state
if "messages" not in st.session_state.keys():
    st.session_state.messages = []
if "model" not in st.session_state.keys():
    st.session_state.model = ChatLLM()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Chat with me!"):
    # User query
    st.session_state.messages.append({"role": "user", "content": prompt}) # Save user message
    with st.chat_message("user"):
        st.markdown(prompt)     # Display user message

    # Assistant response
    with st.chat_message("assistant"): 

        with st.spinner("..."):
            # Display response with typing effect
            placeholder = st.empty()
            full_response = ''
            for item in st.session_state.model.generate_response(prompt): # Simulate typing effect
                full_response += item
                # Simulate typing effect
                placeholder.markdown(full_response)

        # placeholder.markdown(full_response)


    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": full_response})