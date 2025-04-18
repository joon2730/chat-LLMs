from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from datetime import datetime, timezone

_chat_instruction = """\
You are a human chatting casually in an online chat.
Be natural and talk short and concise.
"""

prompt = PromptTemplate(
    input_variables=["current_time"],
    template=_chat_instruction,
)

CHAT_PROMPT = ChatPromptTemplate.from_messages([
    ("system", prompt.format(current_time=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"))),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])