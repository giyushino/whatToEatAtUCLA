from openai import OpenAI
from reformat import create_menus, split 

def deepseek_chat():
    client = OpenAI(api_key="YOUR-API-KEY", base_url="https://api.deepseek.com")

    dining_halls = ["BruinPlate", "DeNeve", "Epicuria"]
    menu_path = r"C:\Users\allan\nvim\python\whatToEatAtUCLA\menu\{}.txt"
    menus = create_menus(menu_path, halls = dining_halls)

    test = split(menus)

    messages = [
            {"role": "system", "content": "You are a helpful chatbot that helps users choose what to eat based on their preferences. You have access to the menus from the following dining halls: {}: {}, {}: {}, {}: {}".format(test[0][0], test[0][1], test[1][0], test[1][1], test[2][0], test[2][1])}
    ]
    print("What would you like to eat? Do you have any preferences or allergies?")
    # Loop to continue the conversation
    while True:
        # Get user input
        user_input = input("Enter: ")
        
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
        print(f"Dining Assistant: {bot_reply}")

        # Add the bot's response to the conversation for context
        messages.append({"role": "assistant", "content": bot_reply})

