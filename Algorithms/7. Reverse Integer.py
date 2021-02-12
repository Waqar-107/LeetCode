class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        
        if x < 0:
            mul = -1
        else:
            mul = 1
        
        x = abs(x)
        
        while x:
            r = x % 10
            x //= 10
            
            ans = ans * 10 + r
        
        ans *= mul
        if ans > (2 ** 31 - 1) or ans < -(2 ** 31):
            return 0
        
        return ans
