import requests
from bs4 import BeautifulSoup
import openpyxl

url_base = 'http://corners.gmarket.co.kr/Bestsellers' #all
url_group = '?viewType=G&groupCode=G' # 01~12
url_type = '06'

url = url_base + url_group + url_type

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li:nth-child(2)
items = soup.select('div.best-list')
lists = items[1].select('ul > li')
output = [['아이템 이름','가격','판매자']]

for index , item in enumerate(lists):
    item_name = item.select_one('a.itemname').text
    item_price = item.select_one('div.s-price strong').text
    # print(index,item_name,item_price)
    link = item.select_one('a.itemname').get('href')
    _res = requests.get(link)
    _soup = BeautifulSoup(_res.content, 'html.parser')
    company = _soup.select_one('#container span.text__seller > a').text
    # print(company)
    output.append([item_name,item_price,company])

print(output)

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
# excel_sheet_2 = excel_file.create_sheet()
excel_sheet.title = 'G-market'
for item in output:
    excel_sheet.append(item)
excel_file.save('gmaket.xlsx')
excel_file.close()