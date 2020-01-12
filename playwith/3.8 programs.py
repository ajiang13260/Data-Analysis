# Question one

# step 1, 爬取短评（翻页）
# step 2, 获取前50个评分（忽略空值，正则表达式）
# step 3, 计算平均值(把文字转换成数据)


import requests,re,time
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
r = requests.get('https://book.douban.com/subject/1084336/comments/', headers = headers)
# print(r.text)
# 不会翻页
soup = BeautifulSoup(r.text,'lxml')
pattern = re.compile(' <span class="user-stars allstar(.*) rating"')
p = re.findall(pattern, r.text)
s = 0
i = 0
for star in p:
    s += int(star)
    i += 1
print(s*2/i/10)