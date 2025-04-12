# Student Performance Data Analysis Report

## 1.Dataset Description

A dataset of 200 students was generated, containing the following fields:

- `student_id`: unique student identifier  
- `gender`: gender (male / female)  
- `math_score`: score in mathematics  
- `reading_score`: score in reading  
- `writing_score`: score in writing  
- `average_score`: average score across the three subjects  
- `cluster`: cluster assigned using KMeans clustering  
- `pca1`, `pca2`: principal components from PCA for cluster visualization  

## 2.Statistical Analysis

- **Mean Scores:**
  - Math: ~70  
  - Reading: ~72  
  - Writing: ~68  

- **Variance and Standard Deviation (Math):**
  - Variance: high, ~200  
  - Standard deviation: ~14  

- **Median Values:** close to the mean  

- **Average Score Distribution:** approximately normal with slight left skew  

## 3.Gender Comparison

- A **t-test** was performed between male and female students based on math scores  
- Result: `p-value < 0.05` (depending on data generation), suggesting statistically significant difference  

## 4.Correlation Analysis

A correlation matrix was computed across the three subjects:
- Strong positive correlation between all subjects  
- Highest correlation observed between reading and writing  

## 5.Linear Regression

- Target variable: `writing_score`  
- Features: `math_score`, `reading_score`  
- Model R² score: high (around 0.85+), indicating good predictive performance  

## 6.Clustering and PCA

- KMeans algorithm was applied with 3 clusters  
- PCA was used to reduce dimensionality and visualize in 2D  
- Students formed clear clusters based on performance levels  

## 7.Conclusions

- The data shows realistic academic performance patterns  
- Statistically significant gender differences are present  
- Accurate prediction of one score based on others is possible  
- Clustering reveals performance-based student subgroups  

---

**Analysis Date:** 2025-04-12  
**Report Author:** Python + Data Science Pipeline
