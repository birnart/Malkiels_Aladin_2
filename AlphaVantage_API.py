import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()
weekly_data = data["Weekly Time Series"]

df = pd.DataFrame.from_dict(weekly_data, orient='index')


df = df.rename(columns={
    "1. open": "Open",
    "2. high": "High",
    "3. low": "Low",
    "4. close": "Close",
    "5. volume": "Volume"
})
df = df.astype({
    "Open": float,
    "High": float,
    "Low": float,
    "Close": float,
    "Volume": int
})

