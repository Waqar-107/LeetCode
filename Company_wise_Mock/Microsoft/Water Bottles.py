class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0
        
        while numBottles:
            ans += numBottles
            empty += numBottles
            
            numBottles = empty // numExchange
            empty -= numBottles * numExchange
            
        return ans
