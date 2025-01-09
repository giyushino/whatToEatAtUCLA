from bs4 import BeautifulSoup

# Parse the HTML file
soup = BeautifulSoup(open(r"C:\Users\allan\nvim\python\whatToEatAtUCLA\html\Epicuria.txt"), "html.parser")

menu_items = soup.find_all('li', class_='menu-item')


f = open(r"C:\Users\allan\nvim\python\whatToEatAtUCLA\menu\Epicuria.txt", "w")

# Process each menu item in this section
for item in menu_items:
    # Extract recipe name
    recipe_name_tag = item.find('a', class_='recipelink')
    recipe_name = recipe_name_tag.get_text(strip=True) if recipe_name_tag else 'No name found'
    
    # Extract description
    description_tag = item.find('div', class_='tt-description')
    description = description_tag.get_text(strip=True) if description_tag else 'No description found'
    
    # Extract dietary information (using a safe approach)
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

    # Print the results for this recipe
    print(f"  Recipe: {recipe_name}")
    print(f"  Description: {description}")
    print("  Dietary Info:")
    for code, label in dietary_info.items():
        print(f"   - {label} ({code})")
    print("-" * 50)

print("=" * 50)  # Separator between sections

f.close()

