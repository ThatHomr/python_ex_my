import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'

re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')

data = soup.select('strong.title')
title = []
score = []

for name in data:
    title.append(name.string.strip())

length = len(title)

for j in range(1, length+1):
    str_score = str(j) + '위'
    score.append(str_score)

movie = list(zip(score, title))
print(movie)