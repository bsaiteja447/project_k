import pandas as pd
import plotly.express as px
# Load the CSV file
df = pd.read_csv("matches.csv")
#fig=px.histogram(df,x="winner",nbins=50,title='winner distribution')
#fig.show()

top_winner=df.groupby('winner')['win_by_runs'].sum().sort_values(ascending=False).head(10)
fig=px.bar(top_winner,x=top_winner.index,y=top_winner.values,title='top 10 teams')
fig.show()
