import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/dsa-tutorial-learn-data-structures-and-algorithms/")

#Parsing the HTML
soup = BeautifulSoup(req.content, 'html.parser')


s = soup.find('div')
content = s.find_all('href')

print(content)
