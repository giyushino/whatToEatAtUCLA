from openai import OpenAI

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key="MY API KEY", base_url="https://api.deepseek.com")

# Set up the initial system message (this can be modified)
messages = [
    {"role": "system", "content": "You are a helpful chatbot that helps users choose what to eat based on their preferences."}
]

# Loop to continue the conversation
while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    # Add the user's message to the conversation
    messages.append({"role": "user", "content": user_input})

    # Send the conversation to the model and get the response
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
        stream=False
    )

    # Get and print the model's response
    bot_reply = response.choices[0].message.content
    print(f"Bot: {bot_reply}")

    # Add the bot's response to the conversation for context
    messages.append({"role": "assistant", "content": bot_reply})

