import pandas as pd
import sqlite3

# 1. Загрузка данных из CSV
df = pd.read_csv('sales_data.csv')

# 2. Создание базы и подключение
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# 3. Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        order_id INTEGER,
        product TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        order_date TEXT
    );
''')

# 4. Загрузка данных в базу
df.to_sql('sales', conn, if_exists='replace', index=False)

# 5. Аналитические SQL-запросы
print("a) Total sales by category:")
query1 = '''
SELECT category, SUM(price * quantity) AS total_revenue
FROM sales
GROUP BY category;
'''
print(pd.read_sql(query1, conn))

print("\nb) Top product by revenue:")
query2 = '''
SELECT product, SUM(price * quantity) AS product_revenue
FROM sales
GROUP BY product
ORDER BY product_revenue DESC
LIMIT 1;
'''
print(pd.read_sql(query2, conn))

print("\nc) Daily order count:")
query3 = '''
SELECT order_date, COUNT(order_id) AS orders_per_day
FROM sales
GROUP BY order_date;
'''
print(pd.read_sql(query3, conn))

conn.close()
