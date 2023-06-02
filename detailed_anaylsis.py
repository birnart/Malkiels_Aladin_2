## -- build sperate classes for multifactor model, capm, etc...

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




