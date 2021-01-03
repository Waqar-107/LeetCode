class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        
        inc = [0] * n
        dec = [0] * n
        
        sz = 0
        for i in range(1, n):
            if A[i] > A[i - 1]:
                sz += 1
            else:
                sz = 0
                
            inc[i] = sz
            
        sz = 0
        for i in range(n - 2, -1, -1):
            if A[i] > A[i + 1]:
                sz += 1
            else:
                sz = 0
            
            dec[i] = sz
        
        ans = 0
        for i in range(n):
            if inc[i] and dec[i]:
                ans = max(ans, inc[i] + dec[i] + 1)
        
        return ans
