import pandas as pd
from textblob import TextBlob
import re

# Загрузка данных
df = pd.read_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task3/reviews.csv")

# Анализ тональности
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.3:
        return "positive"
    elif polarity < -0.3:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["review"].apply(get_sentiment)

# Классификация типа проблемы
def classify_issue(text):
    text = text.lower()
    if re.search(r'broken|refund|quality|doesn\'t work|disappointed|fine', text):
        return "product issue"
    elif re.search(r'delivery|late|packaging', text):
        return "delivery issue"
    elif re.search(r'customer service|support|rude|unhelpful', text):
        return "service issue"
    else:
        return "general"

df["issue_type"] = df["review"].apply(classify_issue)

# Сохранение результата
df.to_csv("/Users/islamnashentaev/Desktop/project coffee/statics/task3/classified_reviews.csv", index=False)
print("✅ File 'classified_reviews.csv' saved with sentiment and issue type.")
