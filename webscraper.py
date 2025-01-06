from bs4 import BeautifulSoup
import requests


diningHalls = ["DeNeve", "Epicuria", "BruinPlate", "Covel", "Feast", "Rendezvous", "TheStudy"]
time = ["Breakfast", "Lunch", "Dinner"]
diningHallLink = "https://menu.dining.ucla.edu/Menus/{diningHall}/{time}"
links = []


for hall in diningHalls:
    for meal in time:
        print(diningHallLink.format(diningHall = hall, time = meal))
        r = requests.get(diningHallLink.format(diningHall = hall, time = meal))
        links.append(r)

print(len(links))


#r = requests.get("https://menu.dining.ucla.edu/Menus/Epicuria/Dinner")
#print(r.status_code)

#soup = BeautifulSoup(r.content, "html.parser")

#print("".join(char for char in soup.prettify() if ord(char) < 128))
