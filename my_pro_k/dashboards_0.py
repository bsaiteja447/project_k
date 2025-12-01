import streamlit as st
import pandas as pd
from eda_4 import *

df = pd.read_csv(r"C:\Users\bsait\Downloads\my_project_k\my_pro_k\ecommerce_10k_cleaned.csv")

st.title("📊 Full EDA Dashboard")

# ------------------------------ 1. UNIVARIATE ------------------------------
st.header("1. Univariate Analysis")

st.subheader("1.1 Price Distribution")
st.plotly_chart(univariant("price"))
st.write("""
**Insights:**
- Prices are spread widely, indicating diverse product pricing.  
- Most values lie in the middle range without extreme skewness.  
- Few unusually high prices suggest potential outliers.  
- Overall, distribution looks fairly uniform across bins.
""")
st.divider()

st.subheader("1.2 Total Amount Distribution")
st.plotly_chart(univariant("total_amount"))
st.write("""
**Insights:**
- Total amount values show a wide range of spending behaviors.  
- Majority of orders fall within moderate purchase amounts.  
- A small portion of very high amounts may indicate bulk orders.  
- Distribution appears slightly right-skewed due to high-value transactions.
""")
st.divider()

st.subheader("1.3 Category Count Bar Chart")
st.plotly_chart(univariant2("category"))
st.write("""
**Insights:**
- Some categories dominate the order volume compared to others.  
- Low-selling categories indicate niche or less-preferred products.  
- High variability suggests customers prefer certain product types strongly.  
- Useful for inventory and marketing optimization.
""")
st.divider()


# ------------------------------ 2. BIVARIATE ------------------------------
st.header("2. Bivariate Analysis")

st.subheader("2.1 Category vs Payment Method")
st.plotly_chart(bivariant("category", "payment_method"))
st.write("""
**Insights:**
- Certain categories show higher dependence on UPI and cards.  
- Cash-on-delivery is still preferred in some product groups.  
- Digital payments dominate across most categories.  
- Payment preference varies slightly by product type.
""")
st.divider()

st.subheader("2.2 Customer Segment vs Revenue Category")
st.plotly_chart(bivariant2("Customer_Segment", "Revenue_Category"))
st.write("""
**Insights:**
- VIP customers contribute the highest share of high revenue orders.  
- Regular customers generate more low and medium revenue.  
- Strong differentiation between customer groups is visible.  
- Useful for targeted marketing segmentation.
""")
st.divider()

# ------------------------------ 3. TIME SERIES ------------------------------
st.header("3. Time Series Analysis")

st.subheader("3.2 Monthly Revenue Trend")
st.plotly_chart(linegraph("order_date"))
st.write("""
**Insights:**
- Revenue fluctuates month-to-month without a strong upward trend.  
- Spikes indicate seasonal demand or promotional periods.  
- No long-term decline, suggesting stable business flow.  
- Useful for planning peak season inventory.
""")
st.divider()


# ------------------------------ 4. MORE UNIVARIATE ------------------------------
st.header("4. More Univariate Plots")

st.subheader("4.1 Discount Distribution")
st.plotly_chart(histogram2("discount"))
st.write("""
**Insights:**
- Most orders have low or moderate discounts.  
- High discount values appear rarely, likely during special sales.  
- Distribution suggests conservative discounting strategy.  
- Lower discounts dominate which helps retain revenue margins.
""")
st.divider()


# ------------------------------ 5. BOXPLOT ANALYSIS ------------------------------
st.header("5. Boxplot Analysis")

st.subheader("5.1 Revenue Across States")
st.plotly_chart(boxplot("state", "Revenue"))
st.write("""
**Insights:**
- Some states show higher revenue ranges than others.  
- Multiple outliers indicate scattered high-value orders.  
- Median revenue varies significantly between states.  
- Helps identify regions contributing strongly to sales.
""")
st.divider()


# ------------------------------ 6. PIE CHARTS ------------------------------
st.header("6. Pie Charts")

st.subheader("6.1 Payment Method Share")
st.plotly_chart(pie_chart("payment_method"))
st.write("""
**Insights:**
- UPI holds the largest share among all payment modes.  
- Credit card usage is also strong, showing trust in digital payments.  
- Cash on Delivery still contributes a noticeable portion.  
- Wallet and Net Banking remain least used.
""")
st.divider()

st.subheader("6.2 State Share")
st.plotly_chart(pie_chart("state"))
st.write("""
**Insights:**
- Few states dominate the total order share.  
- Smaller states contribute minimal order volume.  
- Large share concentration indicates selective market strength.  
- Useful to identify high-priority regions for business expansion.
""")
st.divider()


# ------------------------------ 7. SCATTER PLOTS ------------------------------
st.header("7. Scatter Plots")

st.subheader("7.1 Total Amount vs Revenue by Category")
st.plotly_chart(scatter_plot("total_amount", "Revenue", "category"))
st.write("""
**Insights:**
- Revenue increases with total amount, indicating strong correlation.  
- Categories show visible clustering patterns.  
- High-value purchases create sharp revenue peaks.  
- Useful for identifying high-earning categories.
""")
st.divider()

st.subheader("7.2 Discount vs Revenue")
st.plotly_chart(scatter_plot2("discount", "Revenue"))
st.write("""
**Insights:**
- Discount levels do not strongly correlate with revenue.  
- High revenue occurs even when discount is low.  
- Scattered pattern indicates discount isn't main driver of revenue.  
- Suggests value or category influences revenue more than discount.
""")
st.divider()


# ------------------------------ 8. SEGMENT ANALYSIS ------------------------------
st.header("8. Segment Analysis")

st.subheader("8.1 State-wise Revenues")
st.plotly_chart(seg_anlys())
st.write("""
**Insights:**
- Revenue contribution varies strongly across states.  
- Few states generate the majority of overall revenue.  
- Lower-performing states show significant improvement potential.  
- Helps prioritize region-based marketing and logistics.
""")
st.divider()
