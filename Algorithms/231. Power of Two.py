class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p = 1
        for i in range(32):
            if n == p:
                return True
            
            if n < p:
                break
            
            p *= 2
        
        return False
