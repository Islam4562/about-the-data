import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task2/user_logs.csv")

# Преобразование timestamp в datetime и извлечение дня
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date

# Группировка по user_id и вычисление метрик
user_stats = df.groupby("user_id").agg(
    total_visits=("page", "count"),
    avg_duration=("duration", "mean"),
    unique_days=("date", "nunique"),
    unique_pages=("page", "nunique")
).reset_index()

# Нормализация признаков
scaler = StandardScaler()
X_scaled = scaler.fit_transform(user_stats[["total_visits", "avg_duration", "unique_days", "unique_pages"]])

# Кластеризация
kmeans = KMeans(n_clusters=4, random_state=42)
user_stats["cluster"] = kmeans.fit_predict(X_scaled)

# PCA для визуализации
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
user_stats["pca1"] = X_pca[:, 0]
user_stats["pca2"] = X_pca[:, 1]

# Сохранение результатов
output_path = "/Users/islamnashentaev/Desktop/project coffee/statics/task2/clustered_users.csv"
user_stats.to_csv(output_path, index=False)

# Визуализация
plt.figure(figsize=(10, 6))
for c in sorted(user_stats["cluster"].unique()):
    cluster_data = user_stats[user_stats["cluster"] == c]
    plt.scatter(cluster_data["pca1"], cluster_data["pca2"], label=f"Cluster {c}", s=50)

plt.title("User Clusters based on Behavior")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("/Users/islamnashentaev/Desktop/project coffee/statics/task2/cluster_plot.png")
plt.show()

output_path
