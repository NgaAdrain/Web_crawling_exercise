import requests
from bs4 import BeautifulSoup
import numpy as np

def Scrap(page_num = 100):
    if(page_num > 1000):
        page_num = 1000
    base = 'https://movie.naver.com/movie/point/af/list.nhn?&page='
    site_list = []

    for i in range(page_num):
        site_list.append(base + str(i))
    # crawling 영화 평점 -> 최근꺼 10000개를 구별 => 과거의 30000개를 
    # i = 0

    data = []
    for site in site_list:
        # print(i)
        res = requests.get(site)
        if res.status_code != 200:
            continue
        soup = BeautifulSoup(res.content, 'html.parser')
        # print(soup)
        items = soup.select('td.title')
    
        for item in items:
                # i = i + 1
            score = int(item.select_one('em').get_text())
            comment = item.select_one('br').next_sibling.strip()
            if comment == '' or len(comment) < 4:
                continue

            if score < 8:
                eval = 0

            else:
                eval = 1
            data.append([comment,score,eval])
            # print(i,score)
            # print(i,comment) #previous_sibling/next_sibling : 해당 태그의 앞의 element, 뒤의 element 가져오기 #strip : 공백 줄 제거

    # for item in data:
    #     print(item)
    if len(data) == 0:
        return None

    return np.array(data)
if __name__ == "__main__":
    num_of_list = 105
    d = Scrap(num_of_list)
    # print(type(d))
    # print(d.shape)
    for com in d:
        print(com)
# ============================================================#
# link = 'https://search.shopping.naver.com/best100v2/main.nhn'
# res = requests.get(link)
# soup = BeautifulSoup(res.content, 'html.parser')
# soup = BeautifulSoup(res.content, 'html.parser')
# base = 'https://search.shopping.naver.com/best100v2/detail.nhn?catId=5000000'
# section = soup.find('ul', id='dev_course_list')
# titles = section.find_all('li','course')
# for index, title in enumerate(titles):
#     print(str(index + 1) + '.', title.get_text().split('-')[1].split('[')[0].strip())