import requests
from bs4 import BeautifulSoup

link = 'https://finance.naver.com/sise'
res = requests.get(link)
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select("#popularItemList > li > a")
index = 0

for item in data:
    print(index, item.get_text())
    index = index + 1