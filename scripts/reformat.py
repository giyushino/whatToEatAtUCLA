import os

# Init
base_dir = os.path.dirname(os.path.abspath(__file__))
menu_dir = os.path.join(base_dir, "menu")
dining_halls = ["BruinPlate", "DeNeve", "Epicuria"]

def create_menus(menu_dir, halls = ["BruinPlate", "DeNeve", "Epicuria"]):
    """
    Creates aesthetically pleasing menus from the extracted HTML data 

    Args:
        menu_dir (str): Directory where dining hall menu files are located
        halls (list): List of dining dining_halls
    Returns:
        menus (list): List of dictionaries containing menu information
    """
    dining_halls = halls 
    menus = []
    for hall in dining_halls:
        menu = {}
        with open(menu_dir.format(hall), "r") as f:
            recipe = ""
            description = ""
            dietary_info = ""

            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()  
                if "Recipe" in line:
                    if recipe:  
                        menu[recipe] = {"description": description, "dietary_info": dietary_info}
                    recipe = line.split(":")[1].strip()  
                elif "Description" in line:
                    description = line.split(":")[1].strip()  
                elif "Dietary Info" in line:
                    dietary_info = ""  
                    while True:
                        line = f.readline().strip()  
                        if not line or "-" in line:  
                            break
                        dietary_info += line + " "  

            if recipe:
                menu[recipe] = {"description": description, "dietary_info": dietary_info}

        menus.append(menu)
    return menus


def split(menus):
    """
    Splits the menus into a more readable format
    
    Args:
        menus (list): Output of create_menus, list of dictionaries containing menu information
             format: [{"recipe": {"description": "description", "dietary_info": "dietary_info"}}]
    Returns:
        final (list): List of lists containing dining hall and recipes
             format: [["hall1", ["recipe1", "recipe2", ...]], ["hal2l", ["recipe1", "recipe2", ...]             ], ...]
    """
    final = []
    for i in range(len(menus)):
        menu = menus[i]
        temp = []
        for recipe, _ in menu.items():
            temp.append(recipe)
            #print(f"Recipe: {recipe}")
            #print(f"Description: {details['description']}")
            #print(f"Dietary Info: {details['dietary_info']}")
            #print("---")
        final.append([dining_halls[i], temp])
    return final



#dining_halls = ["BruinPlate", "DeNeve", "Epicuria"]
#menus = create_menus(menu_dir = menu_dir + r"\{}.txt" , halls = dining_halls)
#print(split(menus))
