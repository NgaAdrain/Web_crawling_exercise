import requests

# 본인 네이버 api 사용 id & 비밀키
client_id = 'nUKmKS7F6Lj4H8TEz9x1'
client_secret = '8Kjb7YDmea'

# 참고
# https://developers.naver.com/docs/serviceapi/search/search.md
# https://developers.naver.com/docs/search/shopping/
# https://developers.naver.com/docs/serviceapi/search/blog/

def search(api_link, header_params, data, n_display = 10 , r_sort='sim'):
    result = []
    if n_display < 10:
        print('10개 이상!')
        n_display = 10
    num = n_display % 101
    n_start = 1 # 시작은 1부터!
    query = '?query=' + data
    sort = '&sort=' + r_sort
    if n_display > 100:
        for i in range(int(n_display/100)):
            display = '&display=100'
            start = '&start=' + str(n_start)
            request = naver_open_api + query + display + start + sort
            res = requests.get(request, headers = header_params)
            n_start = n_start + 100
            if res.status_code == 200:
                data = res.json()
                temp = []
                for item in data['items']:
                    temp.append(item)
                result.append(temp)
            else:
                print("Error Code:", res.status_code)
    start = '&start=' + str(n_start)          
    display = '&display=' + str(num)
    request = naver_open_api + query + display + start + sort
    res = requests.get(request, headers = header_params)

    if res.status_code == 200:
        data = res.json()
        result.append(data)

    else:
        print("Error Code:", res.status_code)

    return result



naver_open_api = 'https://openapi.naver.com/v1/search/shop.json'
header_params = {"X-naver-client-id":client_id,"X-naver-client-secret":client_secret}
data = 'HUD'
number = 356
sort = 'sim'
ack = search(naver_open_api, header_params, data, number , sort)
# print(ack)
for dat in ack:
    print(dat)
'''

res = requests.get(naver_open_api+query+display+sort, headers = header_params)

#print(res.text)

if res.status_code == 200:
    data = res.json()
    for index, item in enumerate(data['items']):
        print (index + 1, item['title'], item['link'])
        print (item['lprice'])
else:
    print("Error Code:", res.status_code)
'''