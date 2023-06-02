import yfinance as yf
import pandas as pd
import numpy as np
from randomization import all_picks
## -- build sperate classes for multifactor model, capm, etc...

## Preselection Analysis CLASS - COMPLETE

class Prev_Analysis():

    def __init__(self):
        self.risk_f = 0.0346
        self.preselected_list = pd.read_csv("preselected_stocklist.csv")
        self.preselected_ticker_list = self.preselected_list["Ticker"].values.tolist()
        self.preselected_ticker_list.append("SPY")
        
    
    def show_capm(self):
        return print(self.preselected_list[["Ticker","CAPM"]])

    def show_std(self):
        return print(self.preselected_list[["Ticker","Std_deviation"]])

    def show_beta(self):
        return print(self.preselected_list[["Ticker","Beta"]])

    def show_sharpe(self):
        return print(self.preselected_list[["Ticker","Sharpe Arith"]])

    def show_aar(self):
        return print(self.preselected_list[["Ticker","AAR Arith"]])
    
    def capm_analysis(self):
        dfh = yf.download(self.preselected_ticker_list, period="5y", interval="1wk",
                  ignore_tz=True, prepost=False)["Close"]
        returns = dfh.pct_change()
        aar_arith = returns.mean()*52
        std_deviation = returns.std()
        sharpe_arith = (aar_arith/std_deviation)
        covariance = returns.cov()
        beta = covariance["SPY"]/returns["SPY"].var()
        capm = self.risk_f + beta * (returns["SPY"].mean() - self.risk_f)
        ##  creating comprehensive data frame of anaylsed stocks
        df_analysis = pd.DataFrame({"Ticker": self.preselected_ticker_list, "CAPM": capm, "Beta": beta, "Std_deviation": std_deviation,
                                "Sharpe Arith": sharpe_arith, "AAR Arith": aar_arith})
        return print(df_analysis)

## MultiFactor Class 






# def to_excel(num):
#     df_analysis.to_excel(r'/Users/sebastianhaidinger/code/Personal_Projects/Malkiel_Investment',
#     index=True, sheet_name="Analysis" + num)
def spy_values(api):
   returns_spy = api
   cov_spy = api

def volatility(returns):
  volat_v = returns.std()
  return volat_v

def aar_arithmetic(returns):
    aar_arith_v = returns.mean()*52
    return aar_arith_v


def sharpe_arithimetic(aar_arith_v, volat_v):
  sharpe_v = (aar_arith_v/volat_v)
  return sharpe_v

def covariance(returns):
  cov_v = returns.cov()
  return cov_v

def beta(cov_spy, returns_spy):
   beta_v = cov_spy/returns_spy.var()
   return beta_v

def capm(beta, risk_f, returns_spy):
  capm_v = risk_f + beta * (returns_spy.mean() - risk_f)
  return capm_v


def price_earnings(price, earnings):
    price_earnings_v = price / earnings
    return price_earnings_v

def markt_cap(api):
   markt_cap_v = api

def price_book(api):
   price_book_v = api

# thechnicals?
def moving_average():
   something = 0




