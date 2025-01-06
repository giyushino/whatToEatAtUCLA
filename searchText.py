from bs4 import BeautifulSoup

files = ["DeNeve.txt", "Epicuria.txt", "BruinPlate.txt"]

important_lines = []
f = open(r'C:/Users/allan/nvim/python/whatToEatAtUCLA/html/BruinPlate.txt', 'r')
count = 0
for line in f:
    count += 1
f.close()
print(count)
print(important_lines)





