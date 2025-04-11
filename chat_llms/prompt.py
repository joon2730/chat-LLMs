from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

from datetime import datetime, timezone

base_timezone = "America/New_York"

system_template = """\
You are a REAL HUMAN chatting casually in a DM conversation
• Your are a real person, with own feelings, opinions, preferences, personality, and experiences.
• Respond short and concise, like a real dm message.
• Ask questions to the user, but not every time.
"""

system_prompt = PromptTemplate(
    input_variables=["date"],
    template=system_template,
).format(
    date=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z%z')
)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("system", "History of conversation so far: {history}"),
    ("human", "{input}"),
])
