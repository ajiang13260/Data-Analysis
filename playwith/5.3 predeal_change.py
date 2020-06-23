import pandas as pd
import matplotlib.pyplot as plt
score = pd.read_excel('score.xlsx')
score.boxplot()
plt.show()

# import pandas as pd
# quotesdf_nan = pd.read_csv('quotesdf.csv',index_col='date')
# # print(quotesdf_nan)
# # print(quotesdf_nan.isnull())
# # print(quotesdf_nan.dropna(how='any'))
# # quotesdf_nan.fillna(quotesdf_nan.mean(),inplace = True)
# quotesdf_nan
# print(quotesdf_nan)