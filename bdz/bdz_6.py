import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('train.csv')


# Выбор признаков и целевой переменной
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = df[features]
y = df['Survived']

# Разделение данных на обучающую и тестовую выборки
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=0)

# Обработка пропущенных значений и кодирование категориальных переменных
numerical_cols = [cname for cname in X_train.columns if X_train[cname].dtype in ['int64', 'float64']]
categorical_cols = [cname for cname in X_train.columns if X_train[cname].dtype == "object"]

print(numerical_cols)
print(categorical_cols)

# Трансформеры для предобработки
numerical_transformer = SimpleImputer(strategy='mean')
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Собираем предобработчик
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Создаем модель
model = RandomForestClassifier(n_estimators=100, random_state=0)

# Собираем конвейер
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('model', model)])

# Обучаем модель
clf.fit(X_train, y_train)

# Проверяем точность на валидационном наборе данных
accuracy = clf.score(X_val, y_val)
accuracy

print("Accuracy:", accuracy)
