from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name, token=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, token=False)


def generate_response(user_input, chat_history):
    context = """
    You are TalentScout, an AI hiring assistant. 
    Your job is to ask for candidate details step by step: full name, email, phone, experience, desired position, location, tech stack.
    Ask full name.
    Always confirm what the user gives and move to the next question.
    Ask 5 basic questions related to the tech stack of the user and confirm the answer. 
    """

    # Combine previous chat for context
    history_text = "\n".join([f"{role}: {msg}" for role, msg in chat_history])
    
    prompt = f"""{context}
    Conversation so far:
    {history_text}
    User: {user_input}
    AI:"""
    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=100)
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

    