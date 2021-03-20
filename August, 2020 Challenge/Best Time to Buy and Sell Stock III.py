class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sales1, sales2 = 0, 0
        buy1, buy2 = -math.inf, -math.inf
        
        for i in range(len(prices)):
            buy1 = max(buy1, -prices[i])
            sales1 = max(sales1, buy1 + prices[i])
            
            buy2 = max(buy2, sales1 - prices[i])
            sales2 = max(sales2, buy2 + prices[i])
        
        return sales2
