import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
r = requests.get('https://book.douban.com/subject/1084336/comments/', headers = headers)
print(r.status_code)
# r.encoding='utf-8'
# print(r.text)

# 目前还无法解决UnicodeError的问题
with open('littleprince.md','w') as f:
    f.write(r.text)