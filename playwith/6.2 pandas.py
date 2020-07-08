import pandas as pd

djidf = pd.read_csv('djidf.csv')
quotesdf = pd.read_csv('quotesdf.csv')

# 筛选:djidf中最近一次成交价
# print(djidf.price.mean())

# 求道指成分股中所有股票最近一次成交价大于等于300的公司名
# print(djidf[djidf.price >= 300].name)

# 求道指成分股中股票最近一次成交价大于等于300或小于等于50的公司信息
# 统计美国运通公司2019年度9月份的股票开盘天数
# print(djidf[(djidf.price >= 300) | (djidf.price <= 50)].name)
# print(len(quotesdf(quotesdf.index >= '2019-09-01') ))
# 
print(len(quotesdf[(quotesdf.open >= 130) | (quotesdf.open <= 70)]))
# & (quotesdf.index <= '2019-09-30')]))
print(type(quotesdf.index))
print(type(djidf.price))