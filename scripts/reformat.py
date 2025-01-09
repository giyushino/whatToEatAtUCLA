import os

# Init
base_dir = os.path.dirname(os.path.abspath(__file__))
menu_dir = os.path.join(base_dir, "menu")
diningHalls = ["BruinPlate", "DeNeve", "Epicuria"]

def create_menus(menu_dir, halls):
    """
    Creates aesthetically pleasing menus from the extracted HTML data 

    Args:
        menu_dir (str): Directory where dining hall menu files are located.
        halls (list): List of dining halls.
    
    Returns:
        menus (list): List of dictionaries containing menu information.
    """
    menus = []
    
    # Loop through each dining hall
    for hall in halls:
        menu = {}
        
        # Ensure proper path formatting
        menu_file_path = menu_dir.format(hall)
        
        with open(menu_file_path, "r") as f:
            recipe = ""
            description = ""
            dietary_info = ""

            # Read through the file line by line
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip()  

                # If line contains 'Recipe', store the previous recipe and move on
                if "Recipe" in line:
                    if recipe:  # Avoid overwriting existing recipe
                        menu[recipe] = {"description": description, "dietary_info": dietary_info}
                    recipe = line.split(":")[1].strip()  
                # If line contains 'Description', store the description
                elif "Description" in line:
                    description = line.split(":")[1].strip()  
                # If line contains 'Dietary Info', store the dietary information
                elif "Dietary Info" in line:
                    dietary_info = ""  
                    while True:
                        line = f.readline().strip()  
                        if not line or "-" in line:  # End of dietary info block
                            break
                        dietary_info += line + " "  

            # Add the last recipe to the menu
            if recipe:
                menu[recipe] = {"description": description, "dietary_info": dietary_info}

        # Append the current dining hall's menu to the list
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
        final.append([diningHalls[i], temp])
    return final



#menus = create_menus(menu_dir = menu_dir + r"\{}.txt" , halls = diningHalls)
#print(menus)
#print(split(menus))
