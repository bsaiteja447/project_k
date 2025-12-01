import pandas as pd

# Load the dataset
# Use the full path if your CSV is in another folder
df = pd.read_csv(r"C:\Users\bsait\Downloads\my_project_k\my_pro_k\ecommerce_10k.csv")

# -----------------------------
# 1. View first 5 rows
# -----------------------------
print("----- First 5 Rows -----")
print(df.head(5))

# -----------------------------
# 2. DataFrame info (column names, datatypes, null values, memory usage)
# -----------------------------
print("\n----- DataFrame Info -----")
print(df.info())

# -----------------------------
# 3. Show index range of the DataFrame
# -----------------------------
print("\n----- DataFrame Index -----")
print(df.index)

# -----------------------------
# 4. Show column names
# -----------------------------
print("\n----- Column Names -----")
print(df.columns)

# -----------------------------
# 5. Show 6 random rows
# -----------------------------
print("\n----- Random 6 Rows -----")
print(df.sample(6))

# -----------------------------
# 6. Display data types of each column
# -----------------------------
print("\n----- Data Types -----")
print(df.dtypes)

# -----------------------------
# 7. Shape (Rows, Columns)
# -----------------------------
print("\n----- Shape (Rows, Columns) -----")
print(df.shape)

# -----------------------------
# 8. Check duplicated rows (returns True/False for each row)
# -----------------------------
print("\n----- Duplicated Rows (Boolean Series) -----")
print(df.duplicated())

# -----------------------------
# 9. Total number of duplicated rows
# -----------------------------
print("\n----- Total Duplicates Count -----")
print(df.duplicated().sum())

# -----------------------------
# 10. Statistical summary (numerical columns only)
# -----------------------------
print("\n----- Statistical Summary -----")
print(df.describe())

# -----------------------------
# 11. Missing values count in each column
# -----------------------------
print("\n----- Missing Values in Each Column -----")
print(df.isnull().sum())
