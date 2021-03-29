class Solution:
    def solve(self, x, n):
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n % 2:
            return x * self.solve(x, n - 1)
        
        temp = self.solve(x, n // 2)
        return temp * temp
    
    def myPow(self, x: float, n: int) -> float:
        ans = self.solve(x, abs(n))
        
        if n < 0:
            return 1.0 / ans
        
        return ans
