class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        uno = 1
        dos = 2
        curr = -1
        
        for i in range(3, n + 1):
            curr = uno + dos
            uno = dos
            dos = curr
        
        return curr
