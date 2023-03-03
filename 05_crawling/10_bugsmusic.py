import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'

re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')

data = soup.select('p.title > a')
score = []
name = []
artist = []


for item in data:
    name.append(item.string)

length = len(name)

for j in range(1, length+1):
    str_score = str(j) + '위'
    score.append(str_score)

data = soup.select('p.artist > a')

for item in data:
    artist.append(item.string)

music = list(zip(score, name, artist))

print(music)