# -*- coding: utf-8 -*-
"""
Get quotesdf
 
@author: Dazhuang
"""
 
import requests
import re
import json
import pandas as pd
from datetime import date
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)  
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])     # m = ['[{...},{...},...]']
        quotes = quotes[::-1]
    return  [item for item in quotes if 'type' not in item]

# 与5.1的区别在于，把时间戳改成了常规格式
def f(x):
    return date.strftime(x, '%Y-%m-%d')
     
quotes = retrieve_quotes_historical('AXP')
quotesdf_ori = pd.DataFrame(quotes)
lst = []
lst = list(map(f, list(map(date.fromtimestamp, quotesdf_ori.date)))) #使用了一个map函数进行转换，涉及到date时间函数，具体原理还不太懂
quotesdf_ori.index = lst
quotesdf_m = quotesdf_ori.drop(['adjclose'], axis = 1)
quotesdf = quotesdf_m.drop(['date'], axis = 1)
# print(quotesdf)
quotesdf.to_csv("quotesdf.csv")