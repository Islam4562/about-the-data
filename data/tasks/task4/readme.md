# Customer Request Clustering

This project demonstrates how to automatically categorize customer support requests using unsupervised machine learning. The approach relies on text vectorization with TF-IDF and clustering using the KMeans algorithm.

## Data

The input data (`customer_requests.csv`) contains randomly generated customer messages simulating complaints and inquiries submitted via various channels.

| Column         | Description                       |
|----------------|-----------------------------------|
| request_id     | Unique ID of the request          |
| customer_id    | Customer identifier               |
| timestamp      | Date and time of the request      |
| message        | Raw text of the customer message  |
| channel        | Source of the message             |

## Objective

Automatically group similar customer messages into thematic clusters to:
- Streamline response workflows
- Prioritize recurring issues
- Identify emerging problem areas

## Solution Overview

1. **Text Preprocessing**: Messages are vectorized using TF-IDF.
2. **Clustering**: KMeans identifies common topics in the requests.
3. **Topic Extraction**: Top keywords are extracted from cluster centroids.
4. **Visualization**: PCA is used to reduce dimensionality for 2D plotting of the clusters.

## Tools Used

- Python
- pandas
- scikit-learn
- matplotlib & seaborn

## Outputs

- `clustered_requests.csv` — CSV file with assigned cluster and topic
- `customer_clusters.png` — Visual representation of message groupings

## Future Improvements

- Apply advanced NLP models (e.g., BERT embeddings)
- Use DBSCAN for dynamic clustering
- Integrate into real-time customer service pipelines

---

_This project is a basic yet practical starting point for automating customer service analytics using unsupervised learning._
