import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/AqueeqAzam/DS-and-ML-datasets/main/test.csv")
df.head(4)
df.isnull().sum()
df['experience'].value_counts()
df['experience'].fillna(df['experience'].mode()[0], inplace=True)
df.info()
