class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for arr in accounts:
            ans = max(ans, sum(arr))
        
        return ans
