from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
# from langchain.memory import ConversationBufferMemory
# from langchain.memory import ConversationSummaryMemory

from chat_llms.prompt import CHAT_PROMPT
from chat_llms.config import Config
from chat_llms.utils import options

import random

class ChatLLM:
    def __init__(self):
        self.config = Config()

        self.llm = ChatOllama(
            model=self.config.ollama_model_name,
            temperature=self.config.model_temperature,
            max_tokens=self.config.model_max_tokens,
            streaming=True,
        )
        
        self.store = {} # to store session history

        self.with_history = RunnableWithMessageHistory(
            chain := CHAT_PROMPT | self.llm,
            self.get_session_history,
            input_messages_key="input",
            history_messages_key="history",
        )

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]

    def generate_response(self, user_message, session_id):
        print(f"Request from Session ID: {session_id}")
        return self.with_history.invoke(
            {"input": user_message},
            config={"configurable": {"session_id": session_id}},
        ).content