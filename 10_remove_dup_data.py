import pandas as pd
data = {'name': ['a', 'b', 'c', 'd', 'b', 'f'], 'eng': [3, 5, 2, 7, 5, 4]}
df = pd.DataFrame(data)
df

# check duplicated data
df.duplicated()

# display duplicated data
df['duplicated'] = df.duplicated()
df

# remove duplicated data
df.drop_duplicates()
df.drop_duplicates(inplace=True)
df
