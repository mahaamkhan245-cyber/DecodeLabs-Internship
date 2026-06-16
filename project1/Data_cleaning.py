import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel("raw_dataset.xlsx")

# Fill empty cells with 'Null'
df = df.fillna("Null")

# Standardize date format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Sort dates from oldest to newest
df = df.sort_values(by="Date", ascending=True)

# Recalculate TotalPrice
df["TotalPrice"] = (
    pd.to_numeric(df["Quantity"], errors="coerce")
    * pd.to_numeric(df["UnitPrice"], errors="coerce")
)

# Round TotalPrice to 0 decimal places
df["TotalPrice"] = df["TotalPrice"].round(0)

# Check duplicate Order IDs
duplicate_order_ids = df["OrderID"].duplicated().sum()

# Identify repeat customers
repeat_customers = (
    df["CustomerID"]
    .value_counts()
    .loc[lambda x: x > 1]
    .index
)

df["RepeatCustomer"] = df["CustomerID"].isin(repeat_customers)

# Save cleaned dataset
df.to_excel("cleaned_dataset.xlsx", index=False)

print("Data Cleaning Completed")
print(f"Duplicate Order IDs Found: {duplicate_order_ids}")
print(f"Repeat Customers Found: {len(repeat_customers)}")