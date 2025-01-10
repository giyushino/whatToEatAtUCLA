import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always help users with their questions and requests",
    },
    {"role": "user", "content": "{}".format(input("Enter: "))},
]

while True:
    user_input = input("Enter: ")
    if user_input.lower() in ["bye", "bye!", "thanks", "thanks!"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})
    prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
    print(outputs[0]["generated_text"]) 
    print(f"Dining Assistant: {outputs[0]['generated_text']}") 

    messages.append({"role": "assistant", "content": outputs[0]["generated_text"]})


