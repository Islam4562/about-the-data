Task Description: Dividing Data into Categories for Easy Use
Objective:
The goal of this task is to take a dataset containing random data and divide it into "shelves" (categories) to make it more convenient for further analysis or research purposes. These shelves can be based on characteristics such as age, product category, and other parameters that can be extracted from the data.
Task Steps:
Loading the Data: The input consists of a file with random data containing various attributes such as age, income, product category, and purchase date. The first step is to load this file into the program using the pandas library.
Dividing Data by Age Groups: One of the requirements is to divide the data by age groups. To achieve this, we create age intervals, for example:
0-18 years
19-35 years
36-50 years
51+ years
We use the pd.cut() function to categorize the values in the "age" column into these groups. Each value in the "age" column will be assigned the appropriate age group.
Grouping Data by Product Categories: The next step is to divide the data based on product categories. The dataset might have a column called "category" that contains values such as "Electronics", "Clothing", "Furniture", "Groceries", etc.
We use the groupby() function to group the data by this column. Each group represents a product category.
Saving Data into Separate Files: Once the data is divided by age groups and product categories, each of these groups will be saved into a separate CSV file. These files are named to reflect their content, for example:
Electronics_data.csv — for data related to products in the "Electronics" category.
age_group_0-18.csv — for data on users in the 0-18 age group.
These files are saved to disk, making it easier to work with separate groups of data in the future.
Example of Division:
Let’s say we have a dataset with purchase information:
id	age	income	category	purchase_date
1	25	50000	Electronics	2023-02-15
2	45	80000	Furniture	2024-03-01
3	30	60000	Clothing	2023-06-21
4	17	25000	Toys	2025-01-10
After running the task, we would get:
A file Electronics_data.csv containing data for all purchases in the "Electronics" category.
A file age_group_0-18.csv containing data for users in the 0-18 age group.
A file age_group_19-35.csv containing data for users in the 19-35 age group.
Result:
Each file will contain only the rows of data that belong to the respective category or age group. This division makes it easier to organize the data for further analysis, reporting, or other tasks.
Advantages:
Simplifies data analysis since each file contains only the relevant categories.
Makes it easier to process and filter data for further work.
Convenient when working with large datasets, as dividing them into shelves makes them more manageable.
Conclusion:
This solution automatically and efficiently divides the data into categories, making it easier to work with and enabling more organized data analysis. It helps reduce complexity and enhances the ability to derive useful insights from large volumes of data.
