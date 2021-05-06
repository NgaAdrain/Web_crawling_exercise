import requests
from bs4 import BeautifulSoup

link = 'https://finance.naver.com/world'
res = requests.get(link)
html = res.text
start = html.find('var americaData')
end = html.find('var indexLocation',start)
print(html[start:end])
'''
soup = BeautifulSoup(res.content, 'html.parser')

# data = soup.select("table")
data = soup.select("script")
#americaIndex > thead > tr:nth-child(3) > td.tb_td2
seg = data[17]
# print(seg['language'])
# front = seg.find('"knam"')
# print(front)

end = seg.find("var",front)
seg = seg[front:end+1]

# for item in data:
#     print(item.get_text())
#     # print('지수이름:', item.find('a').get_text(), '현재지수:', item.find('span').get_text(), item.find('em').get_text())
'''