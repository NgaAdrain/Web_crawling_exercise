import requests

open_api = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
serviceKey = '?serviceKey=HhlR2lcOKxNkucWEg9%2BUb1nAGjv2PUeLDLHZCWpzQRo9m%2FhI5Aau2BsJurWv%2B%2F6b1CpR5ML9NXbG%2FeRRLxHq8w%3D%3D'
returnType = '&returnType=json'
numOfRows = '&numOfRows=100'
sidoName = '&sidoName=경남'

res = requests.get(open_api+serviceKey+returnType+numOfRows+sidoName)

# print(res.text)
# json data는 대-소문자 구별하여 호출

if res.status_code == 200:
    data = res.json()
    t = data['response']['body']['items']
    for index, item in enumerate(data['response']['body']['items']):
        print (index, item['khaiValue'])
else:
    print("Error Code:", res.status_code)
