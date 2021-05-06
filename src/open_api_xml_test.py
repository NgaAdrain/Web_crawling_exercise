import requests
from bs4 import BeautifulSoup

open_api = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
serviceKey = '?serviceKey=HhlR2lcOKxNkucWEg9%2BUb1nAGjv2PUeLDLHZCWpzQRo9m%2FhI5Aau2BsJurWv%2B%2F6b1CpR5ML9NXbG%2FeRRLxHq8w%3D%3D'
returnType = '&returnType=xml'
numOfRows = '&numOfRows=100'
sidoName = '&sidoName=경남'
# https://www.data.go.kr/data/15073861/openapi.do
res = requests.get(open_api+serviceKey+returnType+numOfRows+sidoName)
soup = BeautifulSoup(res.content, 'html.parser')

lst = []

# xml데이터는 소문자로 호출

if res.status_code == 200:
    data = soup.find_all('item')
    for item in data:
        temp = []
        stationname = item.find('stationname')
        pm10grade = item.find('pm10grade')
        temp.append(stationname.text)
        temp.append(pm10grade.text)
        lst.append(temp)
        print(stationname.get_text(), pm10grade.get_text())
    # for index, item in enumerate(data['items']):
    #     print (index, item)
else:
    print("Error Code:", res.status_code)   
for l in lst:
    print(l)