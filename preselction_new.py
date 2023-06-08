# import pandas as pd
# from functools import partial
import pandas as pd
from AlphaVantage_API import df
from discrimnators import Discriminators


discriminators = Discriminators()

# Create a list of tuples containing the functions and their additional arguments
args = {
    discriminators.volatility: 1,
    discriminators.aar_arithmetic: 5,
    discriminators.sharpe_arithimetic: 5,
}

filtered_df = []
for i in df:
    if all(args):
        filtered_df.append(i)
        print(i)
    if len(filtered_df) > 20:
        break





# Print the filtered data frame

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











                               # #
                              ## ##
                             #######
                            #########
                             #######
                             #######
                             #######
                             #######
                             #######
                             #######
                             #######
                             #######
                             #######
                             #######
                    #####    #######    #####
                   #######             #######
                  #########           #########
                 ###########         ###########
                  #########           #########
                   #######             #######
                    #####               #####
