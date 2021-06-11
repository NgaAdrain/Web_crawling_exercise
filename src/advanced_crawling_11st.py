import requests
from bs4 import BeautifulSoup
import openpyxl

url_base = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain' #all
url_group = '&cornerNo=' # 1~14
url_type = '10'

url = url_base + url_group + url_type + '#pageNum%%2'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

items = soup.select('#bestPrdList > div > ul.cfix')
item_link = items[0].select('div.store')
print(item_link)
item_list = items[0].select('p')

price_list = items[0].select('strong.sale_price')
output = [['아이템 이름','가격']]
for index, item in enumerate(item_list):
    output.append([item.text,price_list[index].text])

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
# excel_sheet_2 = excel_file.create_sheet()
excel_sheet.title = '11st'
for item in output:
    excel_sheet.append(item)
excel_file.save('11st.xlsx')
excel_file.close()