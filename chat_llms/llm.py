from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

from chat_llms.prompt import CHAT_PROMPT
from chat_llms.config import Config
from chat_llms.utils import options

from langgraph.graph import START, END, StateGraph
from langchain_core.runnables import RunnableLambda
from typing_extensions import TypedDict

import random

class State(TypedDict):
    session_id: str
    user_message: str
    response: str

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

        self.graph = self.build_graph()
    
    # ==== private ====
    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()
        return self.store[session_id]

    def respond_node(self, state: State) -> State:
        session_id = state["session_id"]
        user_message = state["user_message"]

        print(f"Request from Session ID: {session_id}")
        response = self.with_history.invoke(            # Invoke the LLM with history
            {"input": user_message},
            config={"configurable": {"session_id": session_id}},
        ).content

        state["response"] = response    # Set the response in the state
        return state

    def build_graph(self):
        graph_builder = StateGraph(State) # Create a graph builder

        graph_builder.add_node(self.respond_node)  # Add nodes

        graph_builder.add_edge(START, "respond_node")   # Add edges
        graph_builder.add_edge("respond_node", END)

        runnable = graph_builder.compile() # Compile the graph into a runnable
        return runnable

    # ==== public ====
    def generate_response(self, user_message: str, session_id: str) -> str:
        state = State(                      # Create a new state
            session_id=session_id,
            user_message=user_message,
            response="",
        )
        result = self.graph.invoke(state)   # Invoke the graph with the state
        return result["response"]           # return the response