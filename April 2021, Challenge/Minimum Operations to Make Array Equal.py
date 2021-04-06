class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        for i in range(n):
            ans += abs(n - (2 * i + 1))
        
        return ans // 2
