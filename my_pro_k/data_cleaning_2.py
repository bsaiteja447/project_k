import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\bsait\Downloads\my_project_k\my_pro_k\ecommerce_10k.csv")

df = df.drop_duplicates()
df = df.reset_index(drop=True)

df["order_date"] = df["order_date"].astype(str).str.replace("-", "/")

# Proper datetime conversion with day-first format
df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True, errors='coerce')

# Format display as DD/MM/YYYY
df["order_date"] = df["order_date"].dt.strftime("%d/%m/%Y")

print(df)
