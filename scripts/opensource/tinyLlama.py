from transformers import pipeline
from scripts.reformat import create_menus, split
import os
import torch

# Define dining halls and paths
diningHalls = ["DeNeve", "Epicuria", "BruinPlate"]
base_dir = os.path.dirname(os.path.abspath(__file__))
menu_dir = os.path.join(base_dir, "menu")

# Create menus
menus = create_menus(menu_dir=os.path.join(menu_dir, "{}.txt"), halls=diningHalls)
test = split(menus)

# Initialize the pipeline
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

# System message with dining hall information
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who will help people choose what UCLA dining hall they should eat at. You have access to the following information regarding each dining hall. Dining hall 1: {}: {}, Dining hall 2: {}: {}, Dining hall 3: {}: {}. You will only help the user choose what dining hall to eat at depending on what they tell you.".format(
            test[0][0], test[0][1], test[1][0], test[1][1], test[2][0], test[2][1]
        )
    },
    {"role": "user", "content": "What dining halls are there?"},
]

# Generate initial response
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=400, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

# Chat loop
while True:
    user_input = input("Enter: ")
    if user_input.lower() in ["bye", "bye!", "thanks", "thanks!"]:
        print("Goodbye!")
        break

    # Append user input to messages
    messages.append({"role": "user", "content": user_input})

    # Regenerate the prompt with updated messages
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    # Generate response
    outputs = pipe(prompt, max_new_tokens=400, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    print(outputs[0]["generated_text"])

    # Append assistant response to messages
    messages.append({"role": "assistant", "content": outputs[0]["generated_text"]})
