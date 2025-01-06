from bs4 import BeautifulSoup
import requests


#diningHalls = ["DeNeve", "Epicuria", "BruinPlate", "HedrickStudy", "FeastAtRieber", "EpicAtAckerman", "TheStudy"]
diningHalls = ["DeNeve", "Epicuria", "BruinPlate", "FeastAtRieber"]

# Don't forget to remove tomorrow from link in future
diningHallLink = "https://menu.dining.ucla.edu/Menus/{diningHall}/tomorrow"
links = []

for hall in diningHalls:
    if hall != "FeastAtRieber":
        r = requests.get(diningHallLink.format(diningHall = hall))
        links.append([r, hall])
print(links)

"""
for link in links:
    """
    #f = open(r"C:\Users\allan\nvim\python\whatToEatAtUCLA\html\{}.txt".format(link[1]), "w")
"""
    soup = BeautifulSoup(link[0].content, "html.parser")
    f.write("".join(char for char in soup.prettify() if ord(char) < 128))
    f.close()
    print(f"Finished writing {link[1]}")
"""







