from webscraper import access_html, parse 
from model import deepseek_chat

# Initial setup
diningHalls = ["DeNeve", "Epicuria", "BruinPlate"]
diningHallLink = "https://menu.dining.ucla.edu/Menus/{}"
#Set to your own path
output_path = r"\whatToEatAtUCLA\html\{}.txt" 
dining_halls = ["BruinPlate", "DeNeve", "Epicuria"]
menu_path = r"C:\Users\allan\nvim\python\whatToEatAtUCLA\menu\{}.txt"

initial = input("Welcome to What2Eat@UCLA! If you would like to the newest menu information, please type 'yes'. Otherwise, please press any key to continue.\n")

if initial == "yes":
    access_html(diningHalls)
    parse()

while True: 
    look = input("Would you like to read any of the menus? Type the name of the dining hall menu you would like to read \n\nCurrently, we have information on DeNeve, Epicuria, and Bruin Plate. \n\nTo speak with our dining assistant, please type 'chat'. \n")

    if look == "deneve" or look == "DeNeve":
        with open(menu_path.format("DeNeve"), "r") as f:
            print(f.read())
    elif look == "epicuria" or look == "Epicuria":
        with open(menu_path.format("Epicuria"), "r") as f:
            print(f.read())
    elif look == "bruinplate" or look == "BruinPlate" or look == "bplate" or look == "BPlate":
        with open(menu_path.format("BruinPlate"), "r") as f:
            print(f.read())
    elif look == "chat":
        break

print("Now that you have seen the menus, you can ask the chatbot for help on what to eat based on your preferences and allergies. Tell them all about your cravings! (as well as any allergies you may have) \n")

deepseek_chat()


