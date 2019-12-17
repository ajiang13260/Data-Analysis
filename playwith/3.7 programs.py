import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.83 Safari/535.11"}
# r = requests.get('https://movie.douban.com/subject/25887288/comments?status=P', headers = headers)