from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from langchain.memory import ConversationBufferMemory
# from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain

from chat_llms.prompt import CHAT_PROMPT, RANDOM_PERSONA_PROMPT, TONE_INSTRUCTION_PROMPT
from chat_llms.config import Config
from chat_llms.utils import options

import random

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

        # create persona
        self.persona = self.llm.invoke(RANDOM_PERSONA_PROMPT.format(
            # name=random.choice(options.NAMES_LIST),
            personality=random.choice(options.PERSONALITIES_LIST),
            language=self.config.language,
        )).content

        self.tone_instruction = self.llm.invoke(TONE_INSTRUCTION_PROMPT.format(
            persona=self.persona,
        )).content

        # define chat prompt
        self.prompt = CHAT_PROMPT.partial(
            persona=self.persona,
            tone_instruction=self.tone_instruction,
            relationship=random.choice(options.RELATIONSHIPS_LIST),
        )

        # define conversation chain
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=self.prompt,
            verbose=True
        )

    def generate_response(self, user_message):
        for chunk in self.conversation.stream(user_message):
            return chunk['response']