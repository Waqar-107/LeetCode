class Solution:
    def arrangeCoins(self, n: int) -> int:
        req = 1
        while n:
            if req > n:
                break
            
            n -= req
            req += 1
        
        return req - 1
