# Method - 1
def Stock(arr):
    max_profit = 0
    min_price = float('inf')

    for i in range(len(arr)):
        min_price = min(min_price, arr[i])
        max_profit = max(max_profit, arr[i] - min_price)
    return max_profit


arr = [7, 1, 5, 3, 6, 4]
print(Stock(arr))

# ---------------------------------------------------------------

# Method - 2


def StockBuy(prices):
    profit = 0
    buy = prices[0]

    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit


arr = [3, 8, 1, 4, 7, 5]
print(StockBuy(arr))
