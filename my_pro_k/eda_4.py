import pandas as pd
import plotly.express as px
df = pd.read_csv(r"C:\Users\bsait\Downloads\my_project_k\my_pro_k\ecommerce_10k_cleaned.csv")
print(df.columns)

#univarant analysis-price disrtibution,
def univariant(colm_name):
    fig= px.histogram(df,x=colm_name,nbins=50,title=f"distribution of{colm_name}")
    return fig
univariant('price')
univariant('total_amount')

def univariant2(col_name):
    d=df[col_name].value_counts().reset_index()
    d.columns=[col_name,'count']
    fig=px.bar(d,x=col_name,y='count',title=f"bar chart of{col_name}")
    return fig
univariant2('category')

#bivariant
def bivariant(cat1,cat2):
    data=df.groupby([cat1,cat2]).size().reset_index(name='count')
    fig=px.bar(data,x=cat1,y='count',color=cat2,title=f"count of {cat1}per{cat2}")
    return fig
bivariant("category","payment_method")

def bivariant2(cat1,cat2):
    d=df.groupby([cat1,cat2]).size().reset_index(name='count')
    fig=px.bar(d,x=cat1,y='count',color=cat2)
    return fig
bivariant2("Customer_Segment","Revenue_Category")

#line graph
def linegraph(col):
    df[col] = pd.to_datetime(df[col])
    monthly = df.groupby(df[col].dt.to_period("M"))["Revenue"].sum().reset_index()
    monthly[col] = monthly[col].astype(str)
    fig = px.line(monthly, x=col, y="Revenue", markers=True, title="Monthly Revenue Trend")
    return fig
linegraph("order_date")



def histogram2(value):
    fig=px.histogram(df,x=value,nbins=40,title='Discount distribution')
    return fig
histogram2('discount')

def boxplot(c1,v1):
    fig=px.box(df,x=c1,y=v1,title= "Revenue across states")
    return fig
boxplot("state","Revenue")

def pie_chart(col):
    res=df[col].value_counts().reset_index()
    res.columns=["pay_type","count"]
    fig=px.pie(res,names='pay_type',values='count',title="shares of payment_modes")
    return fig
pie_chart("payment_method")
pie_chart("state")

def scatter_plot(v1,v2,v3):
    fig=px.scatter(df,x=v1,y=v2,color=v3,title="Total Amount vs Revenue by Category",hover_data=["product_name"])
    return fig
scatter_plot("total_amount","Revenue","category")

def scatter_plot2(v1,v2):
    fig=px.scatter(df,x=v1,y=v2,title="Total Amount vs Revenue by Category",hover_data=["product_name"])
    return fig
scatter_plot2("discount","Revenue")


#segment analysis

def seg_anlys():
    seg=df.groupby("state")["Revenue"].sum().reset_index()
    fig=px.bar(seg,x="state",y="Revenue",title="state wise revenues")
    return fig
seg_anlys()
