# import required library
import numpy as np
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/AqueeqAzam/DS-and-ML-datasets/main/flight.csv")

# display all rows
df

# display particular raws
df.head(4)

# display shape of dataset
df.shape

# display information of dataset
df.info()

# display discribe of dataset
df.describe()

# determine the dependent variable in 2-dimentional
x = df[['Name', 'Location', 'Destination']]
x

# convert into array format
x = df[['Name', 'Location', 'Destination']].values
x

# determine the independent varibale
y = df['Class']
y

