class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit =0
        minBuy = prices[0]

        for i in range(1,len(prices)):
            sell = prices[i]
            maxProfit = max(maxProfit,sell-minBuy)
            minBuy = min(minBuy,sell)
        return maxProfit