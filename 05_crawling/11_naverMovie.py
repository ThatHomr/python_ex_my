import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/point/af/list.naver'

re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')

data = soup.select('tr > td.ac.num')
num = []
title = []
score = []
review = []

for item in data:
    num.append(int(item.string))

data = soup.select('td.title > a')

for item in data:
    title.append(item.string)

data = soup.select('div.list_netizen_score > em')

for item in data:
    score.append(int(item.string))
    
data = soup.find_all('a', class_ = 'report')
# print(data)

for item in data:
    view = str(item)
    view2 = view.split(', ')[2].replace("'", '')
    review.append(view2)
    
movie = list(zip(num, title, score, review))

print(movie)
# print(review)
