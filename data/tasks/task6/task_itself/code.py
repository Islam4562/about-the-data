import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


# Повторно читаем файл для демонстрации
df = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task6/student_scores.csv")

# 1. Среднее и медиана по каждому предмету
mean_scores = df[["math_score", "reading_score", "writing_score"]].mean()
median_scores = df[["math_score", "reading_score", "writing_score"]].median()

# 2. Дисперсия и стандартное отклонение по математике
math_variance = df["math_score"].var()
math_std = df["math_score"].std()

# 3. t-тест: сравнение баллов по математике между мужчинами и женщинами
male_math = df[df["gender"] == "male"]["math_score"]
female_math = df[df["gender"] == "female"]["math_score"]
t_stat, p_value = stats.ttest_ind(male_math, female_math)

# 4. Гистограмма общего среднего балла
df["average_score"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1)
plt.figure(figsize=(8, 5))
sns.histplot(df["average_score"], bins=20, kde=True)
plt.title("Распределение среднего балла")
plt.xlabel("Средний балл")
plt.ylabel("Количество студентов")
plt.tight_layout()
plt.savefig("/Users/islamnashentaev/Desktop/project coffee/statics/task6/average_score_hist.png")
plt.close()

# 5. Корреляционная матрица
correlation_matrix = df[["math_score", "reading_score", "writing_score"]].corr()

# 6. Линейная регрессия: предсказание writing_score
X = df[["math_score", "reading_score"]]
y = df["writing_score"]
reg = LinearRegression().fit(X, y)
y_pred = reg.predict(X)
r_squared = r2_score(y, y_pred)

# Дополнительно:
# Boxplot по math_score по полу
plt.figure(figsize=(6, 4))
sns.boxplot(x="gender", y="math_score", data=df)
plt.title("Math Score по полу")
plt.tight_layout()
plt.savefig("/Users/islamnashentaev/Desktop/project coffee/statics/task6/math_score_boxplot.png")
plt.close()

# Кластеризация
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(df[["math_score", "reading_score", "writing_score"]])

# PCA для 2D-визуализации
scaler = StandardScaler()
scaled_scores = scaler.fit_transform(df[["math_score", "reading_score", "writing_score"]])
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_scores)
df["pca_1"] = pca_result[:, 0]
df["pca_2"] = pca_result[:, 1]

# Визуализация кластеров
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="pca_1", y="pca_2", hue="cluster", palette="deep")
plt.title("PCA-кластеризация студентов")
plt.tight_layout()
plt.savefig("/Users/islamnashentaev/Desktop/project coffee/statics/task6/pca_clusters.png")
plt.close()

# Вывод результатов
{
    "Средние баллы": mean_scores.to_dict(),
    "Медианы баллов": median_scores.to_dict(),
    "Дисперсия по математике": math_variance,
    "Стандартное отклонение по математике": math_std,
    "T-статистика": t_stat,
    "P-значение": p_value,
    "R² линейной регрессии (предсказание writing_score)": r_squared,
    "Корреляционная матрица": correlation_matrix.to_dict(),
    "Гистограмма среднего балла": "/Users/islamnashentaev/Desktop/project coffee/statics/task6/average_score_hist.png",
    "Boxplot по математике": "/Users/islamnashentaev/Desktop/project coffee/statics/task6/math_score_boxplot.png",
    "PCA-кластеризация (изображение)": "/Users/islamnashentaev/Desktop/project coffee/statics/task6/pca_clusters.png"
}
