import pandas as pd
from AlphaVantage_API import df

df["returns"] = df["Close"].pct_change().dropna()
df["stock_price"] = df["Close"]


