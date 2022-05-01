class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num:
            if num % 2:
                num -= 1
                ans += 1
            
            if num:
                num //= 2
                ans += 1
        
        return ans
            
