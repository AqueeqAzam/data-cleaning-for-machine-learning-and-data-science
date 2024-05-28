import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/AqueeqAzam/DS-and-ML-datasets/main/disbetes.csv")
# display data
df.head(4)

# check null values
df.isnull().sum()
df

# fill null values
df['Insulin'].fillna(df['Insulin'].mean(), inplace=True)
df

# display graph
sns.displot(df['Insulin'])
plt.show()

# Scaling the data
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(df[['Insulin']])
ss.transform(df[['Insulin']])
