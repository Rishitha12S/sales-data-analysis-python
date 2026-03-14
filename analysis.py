import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load dataset
df = pd.read_csv("train.csv", encoding="latin1")

# 2️⃣ Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# 3️⃣ Show first rows
print("First 5 rows:")
print(df.head())

# 4️⃣ Dataset info
print("\nDataset Info:")
print(df.info())

# 5️⃣ Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# 6️⃣ Region wise sales
region_sales = df.groupby("Region")["Sales"].sum()
print("\nRegion Wise Sales:")
print(region_sales)

# 7️⃣ Category wise sales
category_sales = df.groupby("Category")["Sales"].sum()
print("\nCategory Wise Sales:")
print(category_sales)

# 8️⃣ Top 10 products
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:")
print(top_products)

# 9️⃣ Top 10 customers
top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers:")
print(top_customers)

# 🔟 Monthly sales trend
monthly_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# ---------------- GRAPHS ---------------- #

# Region Sales Bar Chart
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig("images/region_sales.png")
plt.show()

# Category Sales Bar Chart
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("images/category_sales.png")
plt.show()

# Monthly Sales Trend Line Chart
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("images/monthly_sales.png")
plt.show()