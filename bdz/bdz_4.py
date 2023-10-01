import pandas as pd

df = pd.read_csv('train.csv')


df['Stripped Name'] = df['Name'].str.strip()
df['Last Name'] = df['Stripped Name'].str.split(',', n=1).str[0]
df['Name With Salutation'] = df['Stripped Name'].str.split(',', n=1).str[1]
df['First Name'] = df['Name With Salutation'].str.split(n=1).str[1]
# df['Last Name'] = df['Name Without Salutation'].str.split(n=1).str[1]

# print(df['Name Without Salutation'])

top_10_names = df['First Name'].value_counts().head(10)
top_10_surnames = df['Last Name'].value_counts().head(10)

print(top_10_names)

print(top_10_surnames)
