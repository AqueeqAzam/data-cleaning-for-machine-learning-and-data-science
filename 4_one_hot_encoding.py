import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("https://raw.githubusercontent.com/AqueeqAzam/DS-and-ML-datasets/main/disbetes.csv")
df.head(3)

# display only one columns
df['Glucose'].unique()

le = LabelEncoder()

# display encoding in form of array
le.fit(df['Glucose'])
le.transform(df['Glucose'])

# display encoding in form of rows and columns
df['encoder_name'] = le.fit_transform(df['Glucose'])
df


