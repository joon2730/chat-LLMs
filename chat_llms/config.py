ollama_models = {
    "gemma": "gemma3:latest",
    "lamma": "huihui_ai/llama3.2-abliterate:latest",
    "nemotron": "nemotron-mini:latest",
    "mymodel": "hf.co/joon2730/Llama-3.2-for-Casual-Conversations"
}

if False:
    ## for blind testing
    import random
    options = ["lamma", "mymodel"]

    seed = input("Enter a seed value (or press Enter for random): ")
    random.seed(seed)  # For reproducibility

    # picked_model = random.choice(options)
    print(f"Selected model: {picked_model}")
else:
    picked_model = "mymodel"

class Config:
    ollama_model_name = ollama_models[picked_model]
    model_temperature = 0.8
    model_max_tokens = 1000
    language = "English"