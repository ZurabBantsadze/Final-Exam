import requests
from bs4 import BeautifulSoup


file = open('sample.html', 'r')
soup = BeautifulSoup(file.read(), "html.parser")

cities = []
to_clear = soup.find('nav', {'id': 'left'}).find_all('ul')
sumnum = 0

for city in to_clear[1].find_all('a'):
    cities.append(city.text)

for i in soup.find('main', {'id': 'center'}).find_all('td'):
  if i.text[0].isdigit():
    sumnum += int(i.text.rstrip(' Students'))

print(sumnum)