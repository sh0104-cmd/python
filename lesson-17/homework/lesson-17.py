# Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

# Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df=df.rename(columns=lambda x: x.strip().lower().replace(' ','_'))

# Print the first 3 rows of the DataFrame
df.head(3)
# Find the mean age of the individuals
mean_age=df['age'].mean()
print('Mean age is:', mean_age)
# Select and print only the 'Name' and 'City' columns
print(df[['first_name','city']])
# Add a new column 'Salary' with random salary values
import numpy as np
np.random.seed(42)  # for reproducibility
df['salary'] = np.random.randint(50000, 120001, size=len(df))
print(df)
# Display summary statistics of the DataFrame

print(df.describe())

import pandas as pd

# Create the data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

# Create the DataFrame
sales_and_expenses = pd.DataFrame(data)

# Display the DataFrame
print(sales_and_expenses)

# Calculate and display the maximum sales and expenses.
# Calculate maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
min_sales=sales_and_expenses['Sales'].min()
# Display the results
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

# Calculate and display the minimum sales and expenses.
min_sales=sales_and_expenses['Sales'].min()
min_expenses=sales_and_expenses['Expenses'].min()

print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# Calculate and display the average sales and expenses.
avg_sales=sales_and_expenses['Sales'].mean()
avg_expenses=sales_and_expenses['Expenses'].mean()

print("Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)

import pandas as pd

# Define the data
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# Create the DataFrame
expenses = pd.DataFrame(data)

# Display the DataFrame
print(expenses)

# Calculate maximum expense per category
expenses['Max_Expense'] = expenses[['January', 'February', 'March', 'April']].max(axis=1)

# Display the category and its maximum expense
print(expenses[['Category', 'Max_Expense']])

# Calculate minimum expense per category
expenses['Min_Expense'] = expenses[['January', 'February', 'March', 'April']].min(axis=1)

# Display the category and its minimum expense
print(expenses[['Category', 'Min_Expense']])

#Calculate and display the average expense for each category.

expenses['Avg_Expense'] = expenses[['January', 'February', 'March', 'April']].mean(axis=1)

# Display the category and its minimum expense
print(expenses[['Category', 'Avg_Expense']])

#make Category column as index.
expenses.set_index('Category')
