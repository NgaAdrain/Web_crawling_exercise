import requests
from bs4 import BeautifulSoup

# link = 'https://search.shopping.naver.com/best100v2/main.nhn'
# res = requests.get(link)
# soup = BeautifulSoup(res.content, 'html.parser')
# soup = BeautifulSoup(res.content, 'html.parser')
base = 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=5000000'
site_list = []

for i in range(9):
    site_list.append(base + str(i))

i = 50000000
for site in site_list:
    print(i)
    i = i + 1
    res = requests.get(site)
    soup = BeautifulSoup(res.content, 'html.parser')
    items = soup.select('#productListArea > ul > li > p > a')
    c = 1
    for item in items:
        print(c, item.get_text())
        c = c + 1

# section = soup.find('ul', id='dev_course_list')
# titles = section.find_all('li','course')
# for index, title in enumerate(titles):
#     print(str(index + 1) + '.', title.get_text().split('-')[1].split('[')[0].strip())