class Discriminators():
  risk_f = 12 ## whatever this is

  def volatility(self, df, max_volat):
    bool(df["returns"].std() < max_volat)

  def aar_arithmetic(self, df, min_arr_a):
    bool(df["returns"].mean()*52 > min_arr_a)

  def sharpe_arithimetic(self, df, min_sharpe):
    bool(df["returns"].mean()*52 / df["return"].std() > min_sharpe)

##  for developing lets stay with these, add others when everything is running

  # def price_earnings(df, max_pe):
  #     return bool(df["price"] / df["earnings"] > max_pe)

#   what would we discriminate here by? is there even a reason
  # def covariance(df, cov_range):
  #   # return bool(df["returns"].cov()
  #   return df.cov()

  # def beta(cov_spy, returns_spy):
  #   beta_v = cov_spy/returns_spy.var()
  #   return beta_v

  # def capm(beta, risk_f, returns_spy):
  #   return bool( risk_f + beta * (returns_spy.mean() - risk_f))
  #   return capm_v




  # def markt_cap(api):
  #   markt_cap_v = api


  # def price_book(api):
  #   price_book_v = api

  # # thechnicals?


  # def moving_average():
  #   something = 0
