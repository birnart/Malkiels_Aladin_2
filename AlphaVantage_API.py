import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

df = pd.DataFrame(data)
df_a = df["Weekly Time Series"].dropna()

df_n = pd.DataFrame(df_a[0],index= df_a.index)
df_n.rename(columns = {"4. close": "Close"}, inplace= True)
print(df_n["Close"])
