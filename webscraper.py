from bs4 import BeautifulSoup
from selenium import webdriver
import requests

diningHalls = ["DeNeve", "Epicuria", "BruinPlate", "Covel", "Feast", "Rendezvous", "TheStudy"]


r = requests.get("https://menu.dining.ucla.edu/Menus/Epicuria/Dinner")
print(r.status_code)

soup = BeautifulSoup(r.content, "html.parser")

print("".join(char for char in soup.prettify() if ord(char) < 128))
