class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        cash = 0
        hold = -prices[0]
        
        for i in range(1, n):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        
        return cash
