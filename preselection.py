##  ---------------------------------------
##  LARGE/SLOW FILE -- RUN MAX ONCE A MONTH
##  ---------------------------------------
import yfinance as yf
import pandas as pd
import numpy as np
##  Parsing CSV
etoro_raw = pd.read_csv("etoro_data.csv")
stock_list = etoro_raw["Ticker"].values.tolist()
stock_list.insert(0, "SPY")


##  Define Risk free Rate
risk_f = 0.0346

##  downloading and calculating Stock and Market returns, volatility, beta, capm etc...
dfh = yf.download(stock_list, period="5y", interval="1wk",
                  ignore_tz=True, prepost=False)["Close"]
returns = dfh.pct_change()
aar_arith = returns.mean()*52
std_deviation = returns.std()
sharpe_arith = (aar_arith/std_deviation)
covariance = returns.cov()
beta = covariance["SPY"]/returns["SPY"].var()
capm = risk_f + beta * (returns["SPY"].mean() - risk_f)
##  creating comprehensive data frame of anaylsed stocks
df_analysis = pd.DataFrame({"Ticker": stock_list, "CAPM": capm, "Beta": beta, "Std_deviation": std_deviation,
                          "Sharpe Arith": sharpe_arith, "AAR Arith": aar_arith})
##  filtering for stocks that outperform market histrically -- ADD VOLATILITY AND RETHINK CAPM MIN
final_df = df_analysis[df_analysis["CAPM"] > capm["SPY"]]

##  exporting selected stocks into new CSV
final_df.to_csv('preselected_stocklist.csv', index=True)

