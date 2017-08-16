# source https://www.interviewcake.com/question/python/stock-price

def get_max_profit(stock_prices):
    if len(stock_prices) <= 1:
        return 0

    buy_val = stock_prices[0]
    sell_val = stock_prices[1]
    prof_val = sell_val - buy_val

    for i in range(1, len(stock_prices)):
        stock_price = stock_prices[i]
        # stop updating buy price before the last index
        if stock_price < buy_val and i < len(stock_prices)-1:
            buy_val = stock_price
            sell_val = stock_prices[i+1]

        elif stock_price > sell_val:
            sell_val = stock_price

        if (sell_val - buy_val) > prof_val:
            prof_val = (sell_val - buy_val)

    return prof_val

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print(get_max_profit(stock_prices_yesterday)) # return 6

stock_prices_yesterday = [10, 7, 5]
print(get_max_profit(stock_prices_yesterday)) # return -2
