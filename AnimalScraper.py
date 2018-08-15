
import re
import requests

from bs4 import BeautifulSoup

# great source for animal names
html = requests.get('https://a-z-animals.com/animals/')
soup = BeautifulSoup(html.text)

titles = [] # title of most links on page are animal names

for link in soup.find_all('a'):
    title = link.get('title')

    if title != None: # link without title has no animal name
        titles.append(title)

# first and last couple of links are not animals
titles = titles[7:-3]

with open('animals.txt', 'w') as animals:
    for animal in titles:
        animals.write('{}\n'.format(animal))