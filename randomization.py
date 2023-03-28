import yfinance as yf
import pandas as pd
import numpy as np
import openpyxl
##  Parsing CSV
etoro_raw = pd.read_csv("preselected_stocklist.csv")
stock_list = etoro_raw["Ticker"].values.tolist()

##  random stock selection and group allocation
stock_num = int(input("How many stocks does every group need?: "))

all_picks = ["SPY"]
for k in range(1,5):
    group_picks = np.random.choice(stock_list,stock_num,replace=False)
    print("Group ", k, "stocks are: ", group_picks)
    all_picks.extend(group_picks)