import tushare as ts
import numpy as np
# 1
df = ts.get_hist_data('600036',start='2019-01-01',end='2019-04-30')
df = df.iloc[:,:5]
print(df)
df_1 = df.sort_index(inplace = True)
print(df_1)