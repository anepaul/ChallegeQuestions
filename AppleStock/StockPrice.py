# source https://www.interviewcake.com/question/python/stock-price

def get_max_profit(stock_prices):
    # Parameter validation
    if len(stock_prices) < 2:
        raise IndexError("Input paramter list does not contain atleast 2 values")

    # Buy values constraint
    buy_val = stock_prices[0]
    # Maximizing Profit
    max_prof = stock_prices[1] - buy_val

    for i in range(1, len(stock_prices)):
        stock_price = stock_prices[i]

        # Check current profit
        profit = stock_price - buy_val
        # Maximize profit
        max_prof = max(profit, max_prof)
        # Remember the largest previous profit but update to the lowest value seen
        buy_val = min(stock_price, buy_val)

    return max_prof

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print(get_max_profit(stock_prices_yesterday)) # return 6

stock_prices_yesterday = [10, 7, 5]
print(get_max_profit(stock_prices_yesterday)) # return -2
