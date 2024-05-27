import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/AqueeqAzam/DS-and-ML-datasets/main/disbetes.csv")
df

# determining the missing content in dataset
df.isnull()

# count the null values
df.isnull().sum()

# calculate the percent of null values
df.isnull().sum()/len(df)*100

# alternative method
df.isnull().sum()/df.shape[0]*100

# to caunt the total values of missing content (null)
df.isnull().sum().sum()

# to caunt the total values of missing content (null) in pencent
df.isnull().sum().sum()/len(df)*100

# count how much not null values present
df.notnull().sum()
