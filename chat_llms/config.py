ollama_models = {
    "gemma": "gemma3:latest",
    "lamma": "huihui_ai/llama3.2-abliterate:latest",
    "nemotron": "nemotron-mini:latest",
}

persona_names = [
    "Erik",
    "Liam",
    "Noah",
    "James",
    "William",
    "Benjamin",
    "Lucas",
    "Henry",
    "Alexander",
    "Charlotte",
    "Amelia",
    "Ava",
    "Sophia",
]

class Config:
    ollama_model_name = ollama_models["lamma"]
    model_temperature = 0.8 # 0 to 1
    model_max_tokens = 2000
    language = "English"