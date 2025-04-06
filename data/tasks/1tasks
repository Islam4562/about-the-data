Task description: Dividing the data into categories for convenient use
The purpose of the task:
The task is to take a set of random data and divide them into "shelves" (categories), which will make it more convenient to use them for further analytical or research purposes. These shelves can be based on characteristics such as age, product category, and other parameters that can be identified in the data.
Task Completion Steps:
Data upload: A file with random data is submitted to the input, which contains various attributes such as age, income, product category and date of purchase. We start by uploading this file to a program using the pandas library.
Separation of data by age groups: One of the requirements of the task is the separation of data by age groups. To do this, we create age ranges, for example:
0-18 years old
19-35 years
old 36-50 years
old 51+ years old
We use the pd.cut() function to divide the age values into these categories. Each value in the "age" column will be assigned a corresponding age group.
Grouping data by product categories: The next step is to separate the data by product category. The dataset may have a "category" column, which may contain values such as "Electronics", "Clothing", "Furniture", "Products", etc.
We use the groupby() function to group data by this column. Each group will represent a separate product category.
Saving data to separate files: After the data is divided by age groups and product categories, each of these groups will be saved to a separate CSV file. This creates files with names reflecting their contents, for example:
Electronics_data.csv — for data on products of the "Electronics" category.
age_group_0-18.csv — for data on users in the age group 0-18 years.
These files are saved on disk, which makes it easy to work with individual groups of data in the future.
Example of separation:
Let's say we have a dataset with information about purchases:
id	age	income	category	purchase_date
1	25	50000	Electronics	2023-02-15
2	45	80000	Furniture	2024-03-01
3	30	60000	Clothing	2023-06-21
4	17	25000	Toys	2025-01-10
As a result of the task, we will receive:
An Electronics_data.csv file with data for all purchases in the Electronics category.
The age_group_0-18.csv file with data for users aged 0 to 18 years.
The age_group_19-35.csv file contains data for users in the 19-35 age group.
Result:
Each file will contain only those data lines that belong to the appropriate category or age group. This separation makes it possible to efficiently organize data for further analysis, reporting, or other tasks.
Advantages:
Simplification of data analysis, since each file contains only the necessary categories.
Ease in processing and filtering data for further work.
It is convenient when working with large datasets, as the division into shelves makes them more manageable.
Conclusion:
Solving the problem allows you to automatically and efficiently categorize data, which helps in further work with them, as well as facilitates the analysis and extraction of useful information from a large amount of data.
