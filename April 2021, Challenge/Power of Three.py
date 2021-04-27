class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            if n % 3:
                return False
            n = n // 3
        
        return True
