# import pandas as pd
# from functools import partial
import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()
from discrimnators import Discriminators
discriminators = Discriminators()


df = pd.DataFrame(data)


# Create a list of tuples containing the functions and their additional arguments
args = {
    discriminators.volatility: 23,
    discriminators.aar_arithmetic: 4,
    discriminators.sharpe_arithimetic: 5,
}
filtered_df = df[df.apply(lambda row: all(
    d(row, args[d]) for d in args), axis=1)]




# Print the filtered data frame
print(filtered_df)

# selection = []
# # Iterate through the functions and apply them to the data frame
# for func, min_value in functions_to_apply:
#     partial_func = partial(func, min_value=min_value)
#     result = partial_func(df)
#     if all(functions_to_apply):
#       selection.append(stock)

#     # Do something with the result (e.g., print it, store it, etc.)
#     print(selection)
# ###

# def preselection(filters, number_of_stocks):
#     for i in range(0,number_of_stocks):
#       for x in filters:
#         yield
#         x(stock, min/max)

#       i = len(selection)


