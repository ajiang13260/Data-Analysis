# import pandas as pd
# df = pd.read_excel("students.xlsx",sheet_name='scores')
# print(df)
# df['sum'] = df["Python"]+df['Math']
# print(df)
# df.to_excel("students.xlsx",sheet_name='scores')

# 两个爬取案例
# 例1 获取道指成分股数据
# 利用request模块和re模块抓取网页源代码，并构建合适的正则表达式，解析获取我们要的数据
# Filename cnn_stock.py
#  -*- coding:utf-8 -*-
# """
# Get djidf
# @author:Dazhuang
# """
# import requests
# import re
# import pandas as pd

# def retrieve_dji_list():
#     try:
#         r = requests.get('https://money.cnn.com/data/dow30/')
#     except ConnectionError as err:
#         print(err)
#     search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*<span.*">(.*?)<\/span>.*\n.*class="wsod_stream">(.*?)<\/span>')
#     dji_list_in_text = re.findall(search_pattern,r.text)
#     dji_list = []
#     for item in dji_list_in_text:
#         dji_list.append({'code':item[0],'name':item[1],'price':float(item[2])})
#     return dji_list

# dji_list = retrieve_dji_list()
# djidf = pd.DataFrame(dji_list)
# # print(djidf)
# djidf.to_csv("djidf.csv")

# 例2 从网站获取一家公司近一年的股票历史数据
# Filename quotes_history.py

# -*- coding: utf-8 -*-
"""
Get quotesdf
 
@author: Dazhuang
"""
import requests
import re
import json
import pandas as pd
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)  
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    # print(m)
    # print(m[0])
    if m:
        quotes = json.loads(m[0])     # m = ['[{...},{...},...]']
        quotes = quotes[::-1]
    return  [item for item in quotes if 'type' not in item]
 
quotes = retrieve_quotes_historical('AXP')
# print(quotes)
quotesdf_ori = pd.DataFrame(quotes)
quotesdf = quotesdf_ori.drop(['adjclose'], axis = 1)
# print(quotesdf)
quotesdf.to_excel("quotesdf.xlsx")
