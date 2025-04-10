import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task4/customer_requests.csv")

# Векторизация текстов
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['message'])

# Кластеризация (например, 5 кластеров)
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster_label'] = kmeans.fit_predict(X)

# Определение ключевых слов для каждого кластера
terms = vectorizer.get_feature_names_out()
top_terms = []
for i in range(5):
    center = kmeans.cluster_centers_[i]
    top_indices = center.argsort()[-3:][::-1]
    top_words = ", ".join(terms[ind] for ind in top_indices)
    top_terms.append(top_words)

df['problem_topic'] = df['cluster_label'].apply(lambda x: top_terms[x])

# Сохранение результата
df.to_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task4/clustered_requests.csv", index=False)

# Визуализация через PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())
df['x'] = X_pca[:, 0]
df['y'] = X_pca[:, 1]

# Построение графика
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='x', y='y', hue='problem_topic', palette='Set2', s=100)
plt.title("Customer Requests Clustering")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend(title="Topic")
plt.grid(True)
plt.tight_layout()
plt.savefig("/Users/islamnashentaev/Desktop/project coffee/statics/task4/customer_clusters.png")
plt.show()
