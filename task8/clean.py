import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from pathlib import Path

base = Path(__file__).resolve().parent

#df = pd.read_csv(f'{base}/Superstore.csv', encoding='utf-8')

with open(f'{base}/Superstore.csv', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

with open(f'{base}new_superstore.csv', 'w', encoding='utf-8') as f:
    f.writelines(lines)

df = pd.read_csv(f'{base}new_superstore.csv')

print(df.head(5))

print(df.info())

print(df.isnull().sum())

print(df.shape)

print(df.columns)

# date format
# changing date datatype from object to datetime.

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y', errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y', errors='coerce')

print(df.info())


# Create new columns for month and year from both date columns
df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year

df['Ship Month'] = df['Ship Date'].dt.month
df['Ship Year'] = df['Ship Date'].dt.year

df['Month Name'] = pd.Categorical(
    df['Order Date'].dt.strftime('%B'),
    categories=['January', 'February', 'March', 'April', 'May', 'June',
                'July', 'August', 'September', 'October', 'November', 'December'],
    ordered=True
)


# Show the updated DataFrame with the new columns
print(df[['Order Date', 'Order Month', 'Month Name', 'Order Year', 'Ship Date', 'Ship Month', 'Ship Year']].head(4))



df.to_csv(f'{base}/superstore_sales_cleaned.csv')

