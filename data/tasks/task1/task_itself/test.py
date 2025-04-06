import pandas as pd
import numpy as np

# Загрузка данных
df = pd.read_csv('/Users/islamnashentaev/Desktop/project coffee/statics/random_data.csv')

# Разделение по возрастным группам
age_bins = [0, 18, 35, 50, 100]  # Возрастные группы
age_labels = ['0-18', '19-35', '36-50', '51+']
df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

# Группировка по категории товара
grouped_by_category = df.groupby('category')

# Разделение на "полки" и сохранение в отдельные файлы
for category, data in grouped_by_category:
    category_file = f"/Users/islamnashentaev/Desktop/project coffee/statics/{category}_data.csv"
    data.to_csv(category_file, index=False)
    print(f"Данные для категории '{category}' сохранены в файл {category_file}")

# Разделение по возрастным группам
grouped_by_age = df.groupby('age_group')

# Сохранение данных по возрастным группам
for age_group, data in grouped_by_age:
    age_group_file = f"/Users/islamnashentaev/Desktop/project coffee/statics/{age_group}.csv"
    data.to_csv(age_group_file, index=False)
    print(f"Данные для возрастной группы '{age_group}' сохранены в файл {age_group_file}")
