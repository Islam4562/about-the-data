# User Behavior Clustering

This project performs behavior-based segmentation of users using log data from a web application.

## Dataset

The dataset is a CSV file containing simulated user activity logs with the following columns:

| Column     | Description                            |
|------------|----------------------------------------|
| user_id    | Unique identifier of the user          |
| timestamp  | Date and time of the page visit        |
| page       | Visited page name                      |
| category   | Page category                          |
| duration   | Time spent on the page (in seconds)    |

**Sample:**


## 🛠️ Solution Overview

The script:
1. Loads and preprocesses the data.
2. Aggregates features per user:
   - Total number of visits
   - Average session duration
   - Number of unique active days
   - Number of unique pages visited
3. Normalizes the features.
4. Applies **KMeans** clustering (4 clusters).
5. Reduces dimensionality using **PCA** for 2D visualization.
6. Saves the clustered user data and cluster plot.

## Outputs

- `clustered_users.csv` — user-level data with assigned cluster labels.
- `cluster_plot.png` — 2D visualization of user clusters.

## Libraries Used

- `pandas` — for data manipulation  
- `scikit-learn` — for clustering and PCA  
- `matplotlib` — for visualization

## How to Use

1. Run the Python script `generate_logs.py` to simulate user data.
2. Run `cluster_users.py` to perform clustering and generate visual output.
3. Check the outputs in the `/mnt/data` directory.

## 💡 Future Improvements

- Use DBSCAN or HDBSCAN for better cluster detection.
- Add sessionization and time-on-site metrics.
- Integrate with real-time log processing pipelines.

---

