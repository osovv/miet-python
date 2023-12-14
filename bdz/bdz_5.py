import pandas as pd

df = pd.read_csv('train.csv')

cols = df.select_dtypes(include=['number']).columns
print(cols)
df[cols] = df[cols].fillna(df[cols].median())

print(df)
