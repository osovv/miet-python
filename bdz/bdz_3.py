import pandas as pd

df = pd.read_csv('train.csv')

survival_by_port = df.groupby('Embarked')['Survived'].agg(['count', 'sum'])

survival_by_port['Survival Rate'] = (survival_by_port['sum'] / survival_by_port['count']) * 100

print(survival_by_port)
