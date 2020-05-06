import requests,re
from bs4 import BeautifulSoup
import time
# Crawl-delay: 5

count = 0
i = 1
s = 0
count_del = 0
lst_stars = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

while count < 50:
    try:
        r = requests.get('https://book.douban.com/subject/1084336/comments/hot?p='+'i', headers = headers)
    except Exception as err:
        print(err)
        break
    
    soup = BeautifulSoup(r.text,'lxml')
    comments = soup.find_all('span','short')

    pattern = re.compile('<span class="user-stars allstar(.*?) rating"')
    p = re.findall(pattern,r.text)

    for item in comments:
        count += 1 #如果爬取的时候count数量没超，但是在这里超了怎么办？
        if count > 50:
            count_del += 1
        # else:
            # print(count,item.string)
    
    for star in p:
        lst_stars.append(int(star))
    
    time.sleep(5)
    # Crawl-delay: 5

    i += 1 #控制页码

    for star in lst_stars[:count_del]:
        s += int(star)
print(p)
print(lst_stars)
print(s,count_del,len(lst_stars))
print('The average star of book is',s//(len(lst_stars)-count_del))