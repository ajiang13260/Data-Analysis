# import requests
# r = requests.get('https://edu-image.nosdn.127.net/0E1CA0462AD847E2F1ECE099FB9F658D.png?imageView&thumbnail=220y62&quality=100')
# with open('pku.png','wb') as fb:
#     fb.write(r.content)

# import requests
# headers = {
#   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
# }
# r = requests.get('https://www.zhihu.com',headers = headers)
# print(r.status_code)
# print(r.text)


# import requests
# from bs4 import BeautifulSoup
# re = requests.get('https://www.icourse163.org/course/WHU-23003')
# soup = BeautifulSoup(re.text,'lxml')
# pattern = soup.find_all('span')
# for item in pattern:
#     print(item.string)

import requests
from bs4 import BeautifulSoup
import re
headers = {
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}
r = requests.get('https://movie.douban.com/subject/33442331/comments?status=P',headers = headers)
pattern = re.compile('<span class="allstar(.*) rating"')
p = re.findall(pattern,r.text)
i = 0
s = 0
for star in p:
    s += int(star)
    i += 1
print(s/i/50*10)