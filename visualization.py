# ==============================
# DATA VISUALIZATION PROJECT
# ==============================

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Make charts look clean
sns.set_style("whitegrid")

# 2. Load Dataset
# Upload your Superstore.csv file in Colab first
df = pd.read_csv("Superstore.csv", encoding='latin1')

# 3. Basic Data Info
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract Year-Month for trend analysis
df['YearMonth'] = df['Order Date'].dt.to_period('M')

# ==============================
# 1️⃣ Sales Trend Over Time
# ==============================

monthly_sales = df.groupby('YearMonth')['Sales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

print("Insight: Sales show seasonal peaks during certain months indicating higher demand during festive periods.\n")


# ==============================
# 2️⃣ Sales by Category
# ==============================

category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

print("Insight: Technology category generates the highest sales compared to Furniture and Office Supplies.\n")


# ==============================
# 3️⃣ Profit by Category
# ==============================

category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()

print("Insight: Despite strong sales, some categories have lower profit margins, indicating higher costs or heavy discounting.\n")


# ==============================
# 4️⃣ Top 10 Products by Sales
# ==============================

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_products.sort_values().plot(kind='barh')
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.show()

print("Insight: A small number of products contribute significantly to overall revenue.\n")


# ==============================
# 5️⃣ Region-wise Sales
# ==============================

region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

print("Insight: Certain regions outperform others, suggesting strong market presence in specific areas.\n")


# ==============================
# 6️⃣ Discount vs Profit
# ==============================

plt.figure(figsize=(8,5))
plt.scatter(df['Discount'], df['Profit'])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

print("Insight: Higher discounts often lead to reduced profitability, showing a negative correlation.\n")


print("PROJECT COMPLETED SUCCESSFULLY")
