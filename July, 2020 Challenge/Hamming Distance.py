class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = bin(x)[2:]
        by = bin(y)[2:]
        
        while len(bx) < len(by):
            bx = '0' + bx
        
        while len(by) < len(bx):
            by = '0' + by
        
        ans = 0
        for i in range(len(bx)):
            if bx[i] != by[i]:
                ans += 1
        
        return ans
