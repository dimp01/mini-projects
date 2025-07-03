# data cleaning
import pandas as pd
import numpy as np
from pathlib import Path

base = Path(__file__).resolve().parent

with open(f'{base}/finance_data.xlsx', 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

with open(f'{base}/new_fin_data.xlsx', 'w', encoding='utf-8') as f:
    f.writelines(lines)

df = pd.read_excel(f'{base}/new_fin_data.xlsx')
print(df.head(5))
