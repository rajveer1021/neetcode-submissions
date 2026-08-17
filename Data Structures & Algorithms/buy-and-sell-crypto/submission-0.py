class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < min_buy :
                min_buy = prices[i]
            profit = prices[i]-min_buy
            max_profit = max(profit, max_profit)
        return max_profit
        