import pandas as pd

df = pd.read_csv('train.csv')

statistics_male = df[df['Sex'] == 'male'].describe()
statistics_female = df[df['Sex'] == 'female'].describe()

print("Male:")
print(statistics_male)

print("\nFemale:")
print(statistics_female)
