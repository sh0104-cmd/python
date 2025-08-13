import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
#Exercise 1: Calculate the average grade for each student.
df1['average_grades']=df1[["Math","English","Science"]].mean(axis=1)
df1[['Student_ID','average_grades']]

#Exercise 2: Find the student with the highest average grade.
# Assuming 'Average_Grade' column has already been added to df1
top_student = df1.loc[df1['average_grades'].idxmax()]

print("Student with the highest average grade:")
print(top_student[['Student_ID', 'average_grades']])

#Exercise 3: Create a new column 'Total' representing the total marks obtained by each student.
df1['Total']=df1[["Math","English","Science"]].sum(axis=1)
df1[['Student_ID','Total']]

#Exercise 4: Plot a bar chart to visualize the average grades in each subject.

import matplotlib.pyplot as plt
# Plot bar chart
plt.figure(figsize=(8, 5))
df1['average_grades'].plot(kind='bar', color='skyblue')

plt.title('Average Grades per Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Grade')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
df2
#Exercise 1: Calculate the total sales for each product.
total_sales=df2[['Product_A','Product_B','Product_C']].sum()
df2
#Exercise 2: Find the date with the highest total sales.
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(),'Date']
print(max_sales_date)

# Calculate percentage change for each product
pct_change_df = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100

# Optionally round for readability
pct_change_df = pct_change_df.round(2)

# Combine with the original date column for context
pct_change_df.insert(0, 'Date', df2['Date'])

print(pct_change_df)
#Exercise 4: Plot a line chart to visualize the sales trends for each product over time.

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Plot each product
plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='s')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='^')

# Add labels, legend, and title
plt.title('Sales Trends for Each Product Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()


import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
#Exercise 1: Average Salary by Department
average_salary = df3.groupby('Department')['Salary'].mean().round(2)
print(average_salary)

#Exercise 2: Employee with the Most Experience
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print(most_experienced)

#Exercise 3: Add 'Salary Increase' Column
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary * 100).round(2)

#Exercise 4: Bar Chart of Employee Distribution by Department
import matplotlib.pyplot as plt

# Count employees per department
dept_counts = df3['Department'].value_counts()

# Plot
plt.figure(figsize=(8, 5))
dept_counts.plot(kind='bar', color='skyblue')

plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

#Exercise 1: Calculate the total revenue from all orders
total_revenue = df4['Total_Price'].sum()
print(f"Umumiy daromad: ${total_revenue}")
#Exercise 2: Find the most ordered product (by quantity)
most_ordered_product = df4.groupby('Product')['Quantity'].sum().idxmax()
print(f"Most Ordered Product: {most_ordered_product}")
#Exercise 3: Calculate the average quantity of products ordered
average_quantity = df4['Quantity'].mean().round(2)
print(f"Average Quantity Ordered: {average_quantity}")

#Exercise 4: Plot a pie chart to visualize the distribution of sales across different products
import matplotlib.pyplot as plt

# Group total sales by product
sales_by_product = df4.groupby('Product')['Total_Price'].sum()

# Plot pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    sales_by_product,
    labels=sales_by_product.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=['#ff9999', '#66b3ff', '#99ff99']
)
plt.title('Sales Distribution by Product')
plt.axis('equal')  # Make it a circle
plt.tight_layout()
plt.show()
