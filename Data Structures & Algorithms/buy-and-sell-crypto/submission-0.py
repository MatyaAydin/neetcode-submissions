class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        l = 0
        r = 1

        while r < len(prices):
            
            buy_price = prices[l]
            sell_price = prices[r]
            diff = prices[r] - prices[l]
            profit = max(profit, diff)
            if buy_price > sell_price:
                l = r

            r += 1

        return profit
        