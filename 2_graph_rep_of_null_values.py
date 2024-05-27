import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/AqueeqAzam/DS-and-ML-datasets/main/disbetes.csv")
df.head(5)
sns.heatmap(df.isnull())
plt.show()
