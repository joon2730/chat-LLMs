from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from langchain.memory import ConversationBufferMemory
# from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain

from chat_llms.prompt import chat_prompt
from chat_llms.config import Config

class ChatLLM:
    def __init__(self):
        self.config = Config()

        self.llm = ChatOllama(
            model=self.config.ollama_model_name,
            temperature=self.config.model_temperature,
            # max_tokens=self.config.model_max_tokens,
            streaming=True,
        )

        self.memory = ConversationBufferMemory()

        self.prompt = chat_prompt

        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=self.prompt,
            verbose=True
        )

    def generate_response(self, user_message):
        for chunk in self.conversation.stream(input=user_message):
            # chunk is of type LLMResult, extract text content
            # print("chunk:", chunk)
            # print(type(chunk))
            return chunk['response']