import tushare as ts
import numpy as np
# 1
df = ts.get_hist_data('600036',start='2019-01-01',end='2019-04-30')
# print(df)
df = df.iloc[:,:5]
# print(df)
df.sort_index(inplace = True)
# print(df)

# 2
# print(df[['high','low']])
# print(df.loc['2019-01-01':'2019-01-31',['high','low']])

# 3
# volume_sorted = df.sort_values(by='volume')
# print(volume_sorted)
# min_day = volume_sorted.iloc[0,:]
# print(min_day)
# min_volume = min_day.volume
# min_volume_date = min_day.name
# print('the min volume of {} is at {}'.format(min_volume,min_volume_date) )
# max_day = volume_sorted.iloc[-1,:]
# print(max_day)
# max_volume = max_day.volume
# max_volume_date = max_day.name
# print('the max volume of {} is at {}'.format(max_volume,max_volume_date) )

# 4
# print(df[df.volume > 100000])

# 5 
# print(len(df[df.close > df.open]))

# 6
# print(df.open.diff())
# print(np.sign(np.diff(df.open)))

# 7
import matplotlib.pyplot as plt
# df_new = df.loc['2019-01-01':"2019-01-31",['high','low']]
# df_new.sort_index().plot()
# plt.show()

# 8 
plt.scatter(df.close-df.open,df.volume)
plt.show()