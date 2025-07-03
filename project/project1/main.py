# data cleaning
import pandas as pd
import numpy as np
from pathlib import Path

base = Path(__file__).resolve().parent

df = pd.read_excel(f'{base}/finance_data.xlsx'); 
print(df.head(5))

print(df.columns)
print(df.info())
print(df.describe().T)
print("Null per column:\n", df.isnull().sum())


# tweaking data
df["Burn_Rate"] = df["Marketing_Spend"] + df["Expenses"] - df["Revenue"]

df["CAC"] = df["Marketing_Spend"] / df["New_Customers"]

df["Avg_Revenue_per_Customer"] = df["Revenue"] / (df["New_Customers"] + df["Retained_Customers"])


# Adjust the lifetime multiplier if you prefer 9 or 12 months
MONTHS_OF_LIFETIME = 6
df["LTV"] = df["Avg_Revenue_per_Customer"] * MONTHS_OF_LIFETIME

df["LTV_CAC_Ratio"] = df["LTV"] / df["CAC"]

df["Run_Rate"] = df["Revenue"] * 12

# month column
df["YearMonth"] = df["Date"].dt.to_period("M")

print(df)

df.to_csv(f"{base}/finance_data.csv")