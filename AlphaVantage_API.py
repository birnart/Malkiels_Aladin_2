import requests
import pandas as pd
from tqdm import tqdm 

## Testing Stock_list 
##REQUIRED: etoro_data.csv
preselected = pd.read_csv("etoro_data.csv")
stock_list = preselected["Ticker"].values.tolist() ## Add only the tickers to the stock list as form of ID
stock_list = stock_list[200:520] ## Use 20 value from the etoro stock_data list

series_list = [] 
## Start the Loop for collecting the Stock data
for n,i in tqdm(enumerate(stock_list)): 
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={i}&apikey=VOBXO7N0MHII7LEJ'
    r = requests.get(url)
    data = r.json()
    try: 
        weekly_data = data["Weekly Time Series"] ## Read the second branch of the json file to obtain the stock data
        dfk = pd.DataFrame.from_dict(weekly_data, orient='index')
        df_new = dfk["4. close"]
        
        series_list.append(df_new)
    except:
        n+1

## Initialize the DataFrame 
df = pd.DataFrame()

## Add the series to the data frame 
for name, series in zip(stock_list, series_list):
    df[name] = series.astype(float)

print(df)    

