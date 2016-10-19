# From O(n^2) to O(n)

def get_max_profit(arg):
    # write the body of your function here
    tn = len(arg)
    cp = []
    profit = 0
    for i in range(tn):
        for m in range(i):
            if i ==m: return
            profit = arg[i]-arg[m]
            cp.append(profit)
    max_profit = max(cp)
    return 'running with %s' % max_profit

def get_max_profit2(stock_prices_yesterday):

    max_profit = 0

    # go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(stock_prices_yesterday):

        # and go through all the LATER prices
        for later_price in stock_prices_yesterday[earlier_time+1:]:

            # see what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit

def get_max_profit3(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    # keep track of the lowest price we have seen so far
    # see if we can get a better profit
    # min_price = stock_prices_yesterday[0]
    # max_profit = 0.0
    for current_price in stock_prices_yesterday:
        # ensure min_price is the lowest price we've seen so far
        min_price = min(current_price, min_price)
        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price
        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
    return max_profit

def get_max_profit4(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    # keep track of the lowest price we have seen so far
    # see if we can get a better profit
    # min_price = stock_prices_yesterday[0]
    # max_profit = 0.0
    for index, current_price in enumerate(stock_prices_yesterday):
        if index ==0:
            continue
        # ensure min_price is the lowest price we've seen so far
        min_price = min(current_price, min_price)
        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price
        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
    return max_profit

# run your function through some test cases here
# remember: debugging is half the battle!
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit4(stock_prices_yesterday)
get_max_profit2(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11))

