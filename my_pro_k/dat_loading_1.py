import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\bsait\Downloads\my_project_k\my_pro_k\ecommerce_10k.csv")
# df = pd.read_csv("ecommerce_10k.csv")  # alternative if CSV is in the same folder

# Data viewing / inspection methods
print(df.head(5))       # first 5 rows
print(df.info())        # info about columns, types, memory, nulls
print(df.index)         # index of the DataFrame
print(df.columns)       # column names
print(df.sample(6))     # 6 random rows
print(df.dtypes)        # data types of columns
print(df.shape)         # (rows, columns)
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().sum())
print(df.describe())     
