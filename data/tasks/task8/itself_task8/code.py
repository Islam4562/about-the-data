import pandas as pd

# Загрузка данных
customers = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task8/task8customers.csv")
product_views = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task8/task8product_views.csv")
orders = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task8/task8orders.csv")
payments = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task8/task8payments.csv")
reviews = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task8/task8reviews.csv")

# Вопрос 1: Категории товаров и возраст
product_views_customers = product_views.merge(customers, on="customer_id")
category_age_stats = (
    product_views_customers.groupby(['category', pd.cut(product_views_customers['age'], bins=[17, 25, 35, 50, 65])])
    .size()
    .reset_index(name='views_count')
)

# Вопрос 2: Сколько заказов и на какую сумму сделал каждый клиент
orders['total_price'] = orders['price'] * orders['quantity']
customer_orders = orders.groupby("customer_id").agg({
    "order_id": "count",
    "total_price": "sum"
}).reset_index().rename(columns={"order_id": "total_orders", "total_price": "total_spent"})

# Вопрос 3: Популярные способы оплаты
payment_stats = payments['payment_method'].value_counts().reset_index()
payment_stats.columns = ['payment_method', 'count']

# Вопрос 4: Связь просмотров и заказов
view_counts = product_views.groupby("product_id").size().reset_index(name="view_count")
order_counts = orders.groupby("product_id").size().reset_index(name="order_count")
views_orders = pd.merge(view_counts, order_counts, on="product_id", how="outer").fillna(0)

# Вопрос 5: Средний рейтинг по категориям и регионам
# сначала объединим reviews с product_views, чтобы получить категории
reviews_with_views = reviews.merge(product_views[['product_id', 'category']], on="product_id", how="left")
reviews_with_customers = reviews_with_views.merge(customers[['customer_id', 'region']], on="customer_id", how="left")
category_region_ratings = reviews_with_customers.groupby(['category', 'region'])['rating'].mean().reset_index()

# Финальный вывод (для демонстрации части результата)
print("--- Популярные категории по возрастам ---")
print(category_age_stats.head())

print("\n--- Заказы клиентов ---")
print(customer_orders.head())

print("\n--- Способы оплаты ---")
print(payment_stats)

print("\n--- Просмотры vs Заказы ---")
print(views_orders.head())

print("\n--- Средний рейтинг по категориям и регионам ---")
print(category_region_ratings.head())
