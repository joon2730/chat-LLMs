model = None

def get_model():
    global model
    if model is None:
        from chat_llms.llm import ChatLLM
        model = ChatLLM()
    return model