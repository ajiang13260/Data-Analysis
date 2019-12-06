import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
r = requests.get('https://www.ipip.net/ip.html',headers=headers)
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span','display: inline-block;text-align: center;width: 720px;float: left;line-height: 46px;')
for item in pattern:
    print(item.string)