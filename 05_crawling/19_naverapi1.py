import urllib.request
import json

client_id = "RBdVS4zChpnpnsSZIe8u"
client_secret = "iFReWhDtuu"
query = input('오타변환 >>> ')
encText = urllib.parse.quote(query)
url = "https://openapi.naver.com/v1/search/errata.json?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
 
data = response_body.decode('utf-8')
result = json.loads(data)
print(result)