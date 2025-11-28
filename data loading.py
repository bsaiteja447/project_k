import pandas as pd

# Load the CSV file
df = pd.read_csv("matches.csv")

# Show basic infoprint(df.info())

# Cleaning data → replacing missing values

#df.dropna(inplace=True)
df.fillna({"umpire3":"petercook"}, inplace=True)
df.drop_duplicates()
#print(df.iloc[:5,:5])
df["date"]=df["date"].astype(str).str.replace("-","/")
df['date']=pd.to_datetime(
    df['date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
    )

df["date"] = df["date"].dt.strftime("%d/%m/%Y")

print(df["date"])
