import pandas as pd
# Load the dataset
df = pd.read_csv('sales_data.csv', parse_dates=['Date'])
# ---------------------------------------------
# Task 1: Group by Category and compute aggregates
category_stats = df.groupby('Category').agg(
    Total_Quantity_Sold=('Quantity', 'sum'),
    Average_Price_Per_Unit=('Price', 'mean'),
    Max_Quantity_Single_Transaction=('Quantity', 'max')
).reset_index()

print("📊 Aggregate statistics by category:")
print(category_stats)

# ---------------------------------------------
# Task 2: Top-selling product in each category (by total quantity sold)
top_products = (
    df.groupby(['Category', 'Product'])['Quantity']
    .sum()
    .reset_index()
    .sort_values(['Category', 'Quantity'], ascending=[True, False])
    .groupby('Category')
    .first()
    .reset_index()
)

print("\n🏆 Top-selling product in each category:")
print(top_products)
# ---------------------------------------------
# Task 3: Date with highest total sales (Quantity * Price)
df['Total_Sale'] = df['Quantity'] * df['Price']

sales_by_date = df.groupby('Date')['Total_Sale'].sum()
top_sales_date = sales_by_date.idxmax()
top_sales_amount = sales_by_date.max()

print(f"\n💰 Date with highest total sales: {top_sales_date.date()} (${top_sales_amount:.2f})")
import pandas as pd
# Load the dataset
df = pd.read_csv('customer_orders.csv')

# -----------------------------------------------------
# Task 1: Group by CustomerID, filter customers with >= 20 orders
customer_order_counts = df.groupby('CustomerID')['OrderID'].nunique()
active_customers = customer_order_counts[customer_order_counts >= 20].index

filtered_customers_df = df[df['CustomerID'].isin(active_customers)]
print("✅ Customers with at least 20 orders:")
print(filtered_customers_df['CustomerID'].unique())

# -----------------------------------------------------
# Task 2: Identify customers who ordered products with average price > $120
avg_price_per_customer = df.groupby('CustomerID')['Price'].mean()
high_spending_customers = avg_price_per_customer[avg_price_per_customer > 120].index

print("\n💸 Customers with average price per unit > $120:")
print(high_spending_customers.tolist())

# -----------------------------------------------------
# Task 3: Total quantity & total price per product, filter products with total quantity >= 5
df['Total_Price'] = df['Quantity'] * df['Price']

product_summary = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Revenue=('Total_Price', 'sum')
).reset_index()

filtered_products = product_summary[product_summary['Total_Quantity'] >= 5]

print("\n📦 Products with total quantity >= 5 units:")
print(filtered_products)

import sqlite3
import pandas as pd
import numpy as np

# --- Step 1: Read data from database ---
db_path = "population.db"
conn = sqlite3.connect(db_path)

# Faqat SELECT ishlatyapmiz
population_df = pd.read_sql_query("SELECT * FROM population;", conn)
conn.close()

# --- Step 2: Read salary band definitions from Excel ---
bands_df = pd.read_excel("population_salary_analysis.xlsx")

# --- Step 3: Categorize salary into bands ---
def get_band(salary):
    for _, row in bands_df.iterrows():
        min_s, max_s = row['MinSalary'], row['MaxSalary']
        if pd.isna(max_s):
            if salary >= min_s:
                return row['Band']
        else:
            if min_s <= salary <= max_s:
                return row['Band']
    return None

population_df['Salary Band'] = population_df['salary'].apply(get_band)

# --- Step 4: Overall stats ---
total_population = len(population_df)

overall_stats = (
    population_df.groupby('Salary Band')
    .agg(
        population_count=('salary', 'count'),
        avg_salary=('salary', 'mean'),
        median_salary=('salary', 'median')
    )
    .reset_index()
)

overall_stats['population_percent'] = (
    overall_stats['population_count'] / total_population * 100
)

# --- Step 5: Stats per state ---
state_stats = (
    population_df.groupby(['state', 'Salary Band'])
    .agg(
        population_count=('salary', 'count'),
        avg_salary=('salary', 'mean'),
        median_salary=('salary', 'median')
    )
    .reset_index()
)

state_totals = (
    population_df.groupby('state')['salary']
    .count()
    .reset_index(name='state_total')
)

state_stats = state_stats.merge(state_totals, on='state')
state_stats['population_percent'] = (
    state_stats['population_count'] / state_stats['state_total'] * 100
)
state_stats.drop(columns='state_total', inplace=True)

# --- Step 6: Save results ---
overall_stats.to_excel("overall_salary_band_analysis.xlsx", index=False)
state_stats.to_excel("statewise_salary_band_analysis.xlsx", index=False)

print("Overall stats:\n", overall_stats)
print("\nState-wise stats:\n", state_stats)
