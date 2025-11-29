import pandas as pd
import numpy as np

# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv(r"C:\Users\bsait\Downloads\my_project_k\my_pro_k\ecommerce_10k.csv")

# -------------------------------
# 2. Drop Duplicates
# -------------------------------
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

# -------------------------------
# 3. Clean order_date
# -------------------------------
df["order_date"] = df["order_date"].astype(str).str.replace("-", "/")
df["order_date"] = pd.to_datetime(
    df["order_date"], 
    format="mixed",
    dayfirst=True,
    errors='coerce'
)
df["order_date"] = df["order_date"].dt.strftime("%d/%m/%Y")

# -------------------------------
# 4. Drop rows with missing values
# -------------------------------
df = df.dropna()
df.reset_index(drop=True, inplace=True)

# -------------------------------
# 5. Categorical Cleaning
# -------------------------------
cat_cols = df.select_dtypes(include=['object', 'category']).columns

# a) Fill missing values with mode
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# b) Capitalize first letters
for col in cat_cols:
    df[col] = df[col].str.title()

# c) Remove extra spaces
for col in cat_cols:
    df[col] = df[col].str.strip()

''' d) Remove special characters (optional)
for col in cat_cols:
    df[col] = df[col].str.replace(r"[^a-z0-9/ ]", "", regex=True)'''

# -------------------------------
# 6. Outlier Removal using IQR
# -------------------------------
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

df.reset_index(drop=True, inplace=True)

# -------------------------------
# 7. BUSINESS COLUMNS
# -------------------------------

# 7a. ORDER SIZE (Small / Medium / Large)
def order_size(amount):
    if amount < 50000:
        return 'Small'
    elif amount < 200000:
        return 'Medium'
    else:
        return 'Large'

df['Order_Size'] = df['total_amount'].apply(order_size)

# 7b. CUSTOMER SEGMENT (VIP / Regular / Low)
customer_total = df.groupby('customer_id')['total_amount'].sum()

def customer_segment(total):
    if total >= 500000:
        return 'VIP'
    elif total > 200000:
        return 'Regular'
    else:
        return 'Low'

df['Customer_Segment'] = df['customer_id'].map(customer_total).apply(customer_segment)

# 7c. DISCOUNT LEVEL (Low / Medium / High)
def discount_level(discount):
    if discount < 2500:
        return 'Low'
    elif discount < 4000:
        return 'Medium'
    else:
        return 'High'

df['Discount_Level'] = df['discount'].apply(discount_level)

# 7d. REVENUE & REVENUE CATEGORY
df['Revenue'] = df['price'] * df['quantity']

def revenue_category(revenue):
    if revenue < 100000:
        return 'Low'
    elif revenue < 400000:
        return 'Medium'
    else:
        return 'High'

df['Revenue_Category'] = df['Revenue'].apply(revenue_category)

# -------------------------------
# 8. Display Business Columns
# -------------------------------
print(df[['order_id', 'total_amount', 'Order_Size', 
          'customer_id', 'Customer_Segment', 
          'discount', 'Discount_Level', 
          'Revenue', 'Revenue_Category']])

# -------------------------------
# 9. Save Cleaned Dataset
# -------------------------------
df.to_csv(r"C:\Users\bsait\Downloads\my_project_k\my_pro_k\ecommerce_10k_cleaned.csv", index=False)
print("Cleaned dataset saved successfully!")
