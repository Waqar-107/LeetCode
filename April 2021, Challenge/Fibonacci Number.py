class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a = 0
        b = 1
        ans = 0
        
        for i in range(2, n + 1):
            ans = a + b
            a = b
            b = ans
        
        return ans
