import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# 1. Загрузка данных
df = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task7/telecom_customers.csv")
print("📊 Data shape:", df.shape)

# 2. Предобработка данных
df.dropna(inplace=True)

# Кодируем категориальные переменные
label_cols = df.select_dtypes(include=['object']).columns.drop(['customer_id'])
label_encoders = {}
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 3. Разделение на X и y
X = df.drop(columns=["customer_id", "churn"])
y = df["churn"]

# 4. Тестовая и обучающая выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Модель RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Предсказание и оценка
y_pred = model.predict(X_test)

print("\n🎯 Accuracy:", accuracy_score(y_test, y_pred))
print("\n📈 Classification Report:\n", classification_report(y_test, y_pred))
print("\n🧩 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 7. Важность признаков
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importances, y=feature_importances.index)
plt.title("📌 Feature Importance")
plt.tight_layout()
plt.show()
