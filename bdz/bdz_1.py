import pandas as pd  

df = pd.read_csv("train.csv")

statistics = df.groupby(['Pclass', 'Sex', 'Survived']).size().unstack(fill_value=0)

print(statistics)
