from bs4 import BeautifulSoup
import requests
import os

# Add other places to eat in the future
diningHalls = ["DeNeve", "Epicuria", "BruinPlate"]

# Base directory dynamically set to the script's location
base_dir = os.path.dirname(os.path.abspath(__file__))
# Dynamically determine output paths
html_dir = os.path.join(base_dir, "html")
menu_dir = os.path.join(base_dir, "menu")  

# Ensure directories exist
os.makedirs(html_dir, exist_ok=True)
os.makedirs(menu_dir, exist_ok=True)


def access_html(diningHalls, html_dir):
    """
    Access the links of each dining hall and create 
    .txt files containing menu information

    Args:
        diningHalls (List[str]) : contains names of dining halls
        html_dir (str) : directory to write .txt files to
    Returns:
        Nothing
    """
    diningHallLink = "https://menu.dining.ucla.edu/Menus/{}"
    for hall in diningHalls:
        r = requests.get(diningHallLink.format(hall))
        output_file = os.path.join(html_dir, f"{hall}.txt")
        
        with open(output_file, "w") as f:
            soup = BeautifulSoup(r.content, "html.parser")
            f.write("".join(char for char in soup.prettify() if ord(char) < 128))
        
        print(f"Extracted {hall}'s webpage data")
    print("=" * 40)

def parse(html_dir, menu_dir):
    """
    Parse the HTML files and extract menu information

    Args:
        html_dir (str): Directory containing saved .txt files containg HTML data
        menu_dir (str): Directory to save parsed menu files
    Returns:
        None
    """
    
    for hall in diningHalls:
        input_file = os.path.join(html_dir, f"{hall}.txt")
        output_file = os.path.join(menu_dir, f"{hall}.txt")
        with open(input_file, "r") as f:
            soup = BeautifulSoup(f, "html.parser")
            
            menu_items = soup.find_all('li', class_='menu-item')

            with open(output_file, "w") as f:
                for item in menu_items:
                    # Extract recipe name
                    recipe_name_tag = item.find('a', class_='recipelink')
                    recipe_name = recipe_name_tag.get_text(strip=True) if recipe_name_tag else 'No name found'
                    
                    # Extract description
                    description_tag = item.find('div', class_='tt-description')
                    description = description_tag.get_text(strip=True) if description_tag else 'No description found'
                    
                    # Extract dietary information
                    dietary_info = {}
                    dietary_info_tags = item.find_all('div', class_='tt-prodwebcode')
                    
                    for tag in dietary_info_tags:
                        dietary_label = tag.get_text(strip=True) if tag else None
                        img_tag = tag.find('img')
                        dietary_code = img_tag.get('alt') if img_tag else None
                        if dietary_label and dietary_code:
                            dietary_info[dietary_code] = dietary_label
                    
                    f.write(f"Recipe: {recipe_name}\n")
                    f.write(f"Description: {description}\n")
                    f.write("Dietary Info:\n")
                    for code, label in dietary_info.items():
                        f.write(f"  - {label} ({code})\n")
                    f.write("-" * 50 + "\n")

                print(f"Successfully obtained {hall}'s menu")

     
 
#access_html(diningHalls, html_dir)
#parse(html_dir, menu_dir)



