import pandas as pd
df = pd.DataFrame({'Size': ['s', 'm', 'l', 'xl', 's', 's', 'l', 'm']})
df.head(4)

# ordinal encoding
from sklearn.preprocessing import OrdinalEncoder
ordi_data = [['s', 'm', 'l', 'xl']]
oe = OrdinalEncoder(categories=ordi_data)
df['Size_en'] = oe.fit_transform(df[['Size']])
df
