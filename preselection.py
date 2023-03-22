import yfinance as yf
import pandas as pd
import numpy as np
import openpyxl
##  Parsing CSV
etoro_raw = pd.read_csv("etoro_data.csv")
stock_list = etoro_raw["Ticker"].values.tolist()
test_list = stock_list[500:510]
test_list.insert(0,"SPY")
print(test_list)

##  Define Risk free Rate
risk_f = 0.0346

# Stock+Market returns and Download
dfh = yf.download(test_list, period="5y", interval="1wk",
                  ignore_tz=True, prepost=False)["Close"]
dfh2 = dfh.dropna(1)
returns = dfh2.pct_change()
mrt_ret = returns.loc[:,"SPY"]
aar_arith = returns.mean()*52
std_deviation = returns.std()
sharpe_arith = (aar_arith/std_deviation)
covariance = returns.cov()
beta = covariance["SPY"]/returns["SPY"].var()
print(beta)
capm = risk_f + beta * (mrt_ret - risk_f)
#print(capm)
schwellenwert = capm.loc["SPY"]
df_analysis = pd.DataFrame({"Stock Ticker": test_list, "CAPM": capm, "Beta": beta, "Std_deviation": std_deviation,
                          "Sharpe Arith": sharpe_arith, "AAR Arith": aar_arith})

print(df_analysis)
# print(df_analysis[df_analysis["CAPM"] > schwellenwert])
# print(final_df)


# final_df.to_csv('preselected_stocklist.csv', index=True)

# def to_excel(num):
#     df_analysis.to_excel(r'/Users/sebastianhaidinger/code/Personal_Projects/Malkiel_Investment',
#                          index=True, sheet_name="Analysis" + num)

# to_excel(str(1))
