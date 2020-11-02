class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        amounts = [math.inf] * (amount + 1)
        amounts[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                remain_amount = i - c
                
                if remain_amount >= 0 and amounts[remain_amount] != math.inf:
                    amounts[i] = min(amounts[i], 1 + amounts[remain_amount])
        
        if amounts[amount] == math.inf:
            return -1
        
        return amounts[amount]
