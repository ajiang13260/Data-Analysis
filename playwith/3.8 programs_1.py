# Question one

# step 1, 爬取短评（翻页）
# step 2, 获取前50个评分（忽略空值，正则表达式）
# step 3, 计算平均值(把文字转换成数据)


# import requests,re,time
# from bs4 import BeautifulSoup

# headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
# r = requests.get('https://book.douban.com/subject/1084336/comments/', headers = headers)
# # print(r.text)
# # 不会翻页
# soup = BeautifulSoup(r.text,'lxml')
# pattern = re.compile(' <span class="user-stars allstar(.*?) rating"')
# p = re.findall(pattern, r.text)
# s = 0
# i = 0
# for star in p:
#     s += int(star)
#     i += 1
# print(s*2/i/10)


# 参考代码1:将url中的bookid换成自己想查看的书的id，例如1084336
# -*-coding:utf-8-*-

"""
Comments parsing
@author:Dazhuang
"""

import requests,re,time
from bs4 import BeautifulSoup

count = 0
i = 0
s, count_s, count_del = 0, 0, 0
lst_stars = []

headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
while count < 50:
    try:
        r = requests.get('https://book.douban.com/subject/1084336/comments/', headers = headers)
        count += 1
    except Exception as err:
        print(err)
        break
    soup = BeautifulSoup(r.text,'lxml')
    comments = soup.find_all('span','short')
    pattern = re.compile(' <span class="user-stars allstar(.*?) rating"')
    
    # Other way
