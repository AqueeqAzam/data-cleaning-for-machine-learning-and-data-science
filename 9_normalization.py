import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("https://raw.githubusercontent.com/AqueeqAzam/DS-and-ML-datasets/main/disbetes.csv")

dataset.isnull().sum()
dataset.describe()

sns.distplot(dataset['Insulin'])
plt.show()

from sklearn.preprocessing import MinMaxScaler
mx = MinMaxScaler()
mx.fit_transform(df[['Insulin']])
df.head()
