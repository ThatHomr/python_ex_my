from urllib import request
from bs4 import BeautifulSoup
import re

data = []

for i in range(1, 11):
    url = f'https://movie.naver.com/movie/point/af/list.naver?page={i}'
    resp = request.urlopen(url)
    soup = BeautifulSoup(resp, 'html.parser')
    # print(soup)
    table = soup.find('table', class_ = 'list_netizen')
    for i, r in enumerate(table.select('tbody tr')):
        # print(i)
        # print(r)
        for j,c in enumerate(r.find_all('td')):
            # print(j)
            # print(c)
            if j == 0:
                # print('글번호 : ' + c.string.strip())
                no = int(c.string.strip())
            elif j == 1:
                # print('제목 : ' + c.select_one('a').string.strip())
                title = c.select_one('a').string.strip()
                # print('평점 : ' + c.select_one('em').string.strip())
                score = int(c.select_one('em').string.strip())
                
                review = c.text
                review = review.replace(title, '')
                review = review.replace('신고', '')
                review = re.sub('별점 - 총 10점 중[0-9]{1,2}', '', review).strip()
                # print('영화평 : ' + review)
            
            try : 
                movie_dic = {'제목' : title, '평점' : score, '영화평' : review}
                data.append(movie_dic)
            except Exception:
                continue
            
print(data)    
    