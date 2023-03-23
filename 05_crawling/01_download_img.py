from urllib import request

url = 'https://pds.joongang.co.kr/news/FbMetaImage/202212/0e5449f1-442b-441e-b623-5e8a9eacf6ab.jpg'

filename = '05_crawling/down/siba.jpg'

request.urlretrieve(url, filename)

