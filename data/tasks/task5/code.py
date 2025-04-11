import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Загрузка данных
df = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task5/fraudulent_transactions.csv")

# 2. Предобработка
df['transaction_time'] = pd.to_datetime(df['transaction_time'])
df['hour'] = df['transaction_time'].dt.hour
df['day_of_week'] = df['transaction_time'].dt.dayofweek

# Кодирование категориальных признаков
le = LabelEncoder()
for col in ['merchant', 'device_type', 'location']:
    df[col] = le.fit_transform(df[col])

# 3. Формирование признаков и целевой переменной
X = df[['customer_id', 'amount', 'merchant', 'device_type', 'location', 'hour', 'day_of_week']]
y = df['is_fraud']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Обучение модели
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Предсказание
y_pred = model.predict(X_test)

# 6. Оценка модели
print("=== Classification Report ===")
print(classification_report(y_test, y_pred))

print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

# (Опционально) Визуализация важности признаков
importances = model.feature_importances_
features = X.columns
sns.barplot(x=importances, y=features)
plt.title("Feature Importance")
plt.show()
