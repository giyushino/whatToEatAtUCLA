from scripts.webscraper import access_html, parse 
from scripts.model import deepseek_chat
import os 
from dotenv import load_dotenv
load_dotenv()


#*******************************
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#*******************************

# Initial setup
diningHalls = ["DeNeve", "Epicuria", "BruinPlate"]
diningHallLink = "https://menu.dining.ucla.edu/Menus/{}"
base_dir = os.path.dirname(os.path.abspath(__file__))
html_dir = os.path.join(base_dir, "html")
menu_dir = os.path.join(base_dir, "menu")


initial = input("Welcome to What2Eat@UCLA! If you would like to the newest menu information, please type 'yes'. Otherwise, please press any key to continue.\n")

if initial == "yes":     
    access_html(diningHalls, html_dir)
    parse(html_dir, menu_dir)
    print("Menu information has been updated. \n")

while True: 
    look = input("Would you like to read any of the menus? Type the name of the dining hall menu you would like to read \n\nCurrently, we have information on DeNeve, Epicuria, and Bruin Plate. \n\nTo speak with our dining assistant, please type 'chat'. \n")

    menu_dir = menu_dir + r"\{}.txt"
    if look == "deneve" or look == "DeNeve":
        with open(menu_dir.format("DeNeve"), "r") as f:
            print(f.read())
    elif look == "epicuria" or look == "Epicuria":
        with open(menu_dir.format("Epicuria"), "r") as f:
            print(f.read())
    elif look == "bruinplate" or look == "BruinPlate" or look == "bplate" or look == "BPlate":
        with open(menu_dir.format("BruinPlate"), "r") as f:
            print(f.read())
    elif look == "chat":
        break

print("Now that you have seen the menus, you can ask the chatbot for help on what to eat based on your preferences and allergies. Tell them all about your cravings! (as well as any allergies you may have) \n")


menu_dir = os.path.join(base_dir, "menu")
deepseek_chat(menu_dir, diningHalls, OPENAI_API_KEY)
