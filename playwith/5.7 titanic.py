# import seaborn as sns
import pandas as pd

# titanic_df = sns.load_dataset('titanic')
# print(titanic_df)
# titanic_df.to_csv('titanic.csv')
titanic_df = pd.read_csv('titanic.csv')
# print(titanic_df)

# import matplotlib.pyplot as plt
# plt.bar(titanic_df['age'],titanic_df['pclass'])
# plt.scatter(range(891),titanic_df['age'])
# titanic_df.loc[:891,'age'].plot(kind='bar',color='g')
# plt.hist(titanic_df['age'],bins=10)
# titanic_df['survived'].value_counts().plot(kind='pie')
# plt.show()

# print(titanic_df.sample(n=10))
# print(titanic_df.sample(frac=0.3))

print(titanic_df.iloc[:,4].describe())