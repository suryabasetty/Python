def maxProfit(self, prices):
    if len(prices) == 1:
        return 0
    index = 1
    min_left = [0] * len(prices)
    min_left[0] = sys.maxsize
    min_value = prices[0]
    while index < len(prices):
        min_left[index] = min_value
        min_value = min(min_value, prices[index])
        index += 1
    ans = 0
    index = 0
    while index < len(prices):
        profit = prices[index] - min_left[index]
        ans = max(ans, profit)
        index += 1
    return ans