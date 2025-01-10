from openai import OpenAI
import os
from scripts.reformat import create_menus, split
from dotenv import load_dotenv
load_dotenv()

#*******************************
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#*******************************
# Initialize the base and menu directory 
base_dir = os.path.dirname(os.path.abspath(__file__))
menu_dir = os.path.join(base_dir, "menu")
diningHalls = ["DeNeve", "Epicuria", "BruinPlate"]


def deepseek_chat(menu_dir, halls=diningHalls, OPENAI_API_KEY=OPENAI_API_KEY):
    """
    A chatbot to help users choose meals based on preferences.
    
    Args:
        menu_dir (str): Directory where dining hall menu files are located.
        halls (list): List of dining halls to consider.

    Returns:
        None
    """

    client = OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.deepseek.com")
    menus = create_menus(menu_dir = menu_dir + r"\{}.txt" , halls = diningHalls)
    test = split(menus)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful chatbot that helps users choose what to eat based on their preferences. You have access to the menus from the following dining halls: {}: {}, {}: {}, {}: {}".format(
                test[0][0], test[0][1], test[1][0], test[1][1], test[2][0], test[2][1]
            )
        }
    ]

    print("What would you like to eat? Do you have any preferences or allergies?")
    
    while True:
        user_input = input("Enter: ")

        if user_input.lower() == "bye" or user_input.lower() == "bye!" or user_input.lower() == "thanks" or user_input.lower() == "thanks!":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
             model="deepseek-chat",
             messages=messages,
             max_tokens=1024,
             temperature=0.7,
             stream=False
        )
        bot_reply = response.choices[0].message.content
        
        print(f"Dining Assistant: {bot_reply}") 

        messages.append({"role": "assistant", "content": bot_reply})

#deepseek_chat(menu_dir, halls = diningHalls, OPENAI_API_KEY = OPENAI_API_KEY)


