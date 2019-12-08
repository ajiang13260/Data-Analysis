# -*-coding:utf-8-*-
"""
Crawler

@author:Dazhuang
"""
# import requests
# r = requests.get('https://www.alibabacloud.com/s/zh?type=doc&rangeinfo=h_pid_35468&k=%E7%BD%91%E7%AB%99%E8%B4%9F%E8%B4%A3%E4%BA%BA%E5%92%8C%E6%B3%95%E4%BA%BA%E5%8F%AF%E4%BB%A5%E6%98%AF%E5%90%8C%E4%B8%80%E4%B8%AA%E4%BA%BA%E5%90%97')
# print(r.status_code)
# print(r.text)

# Filename:dji.py
# import requests
# re = requests.get('http://money.cnn.com/data/dow30') # the url may change
# print(re.text)
# print(re.content)
# print(re.json())

# import requests

# r = requests.get('https://wwww.baidu.com/img/bd_logo1.png')
# with open('baidu.png', 'wb') as fp:
#     fp.write(r.content)

# import requests
# re = requests.get('https://www/zhihu.com')
# print(re.status_code)
# # headers 可从http测试网站https://httpbin.org 或浏览器的“开发者工具”获得
# headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
# re = requests.get('https://www.zhihu.com', headers = headers)
# print(re.status_code)

# from bs4 import BeautifulSoup
# makeup = '<p class="title"><b>The Little Price</b></p>'
# soup = BeautifulSoup(makeup, 'lxml')
# # print(soup.b)
# print(type(soup.b))
# tag = soup.p
# print(tag.name)
# print(tag.attrs)
# print(tag['class'])
# print(tag.string)
# print(type(tag.string))
# print(soup.find_all('b'))
# print(soup.find('b'))

# import requests
# from bs4 import BeautifulSoup
# headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
# r = requests.get('https://y.qq.com/n/yqq/playlist/1488252888.html#comment_box',headers=headers)
# print(r.status_code)
# soup = BeautifulSoup(r.text, 'lxml')
# print(r.text)
# pattern = soup.find_all('p','c_tx_normal comment__text js_hot_text')
# for item in pattern:
#     print(item.string)

# -*-coding:utf-8-*-
"""
Crawler

@author:Ajiang
"""
# import requests
# from bs4 import BeautifulSoup
# import re

# s = 0
# headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
# r = requests.get('https://movie.douban.com/subject/25887288/comments?status=P', headers = headers)
# print(r.status_code)
# soup = BeautifulSoup(r.text, 'lxml')
# pattern = soup.find_all('span','short')
# for item in pattern:
#     print(item.string)
# pattern_s = re.compile('<span class="allstar(.*?) rating"')
# p = re.findall(pattern_s, r.text)
# for star in p:
#     s += int(star)
# print(s)


import requests
r = requests.get('https://www.speedycloud.cn/')
print(r.text)
