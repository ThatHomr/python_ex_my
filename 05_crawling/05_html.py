import requests

query = input('검색할 키 >>> ')
api = 'https://search.naver.com/search.naver'
values = {
# 'sm' : 'tab_hty.top',
# 'where' : 'nexearch',
'query' : query
# 'oquery' : '벚꽃',
# 'tqi' : 'iss46wprvN8ssZSUmBNssssstoG-506591'
# acq = '벚꽃'
# acr = 4
# qdt = 0
}

r = requests.get(api, params=values)
print(r.text)