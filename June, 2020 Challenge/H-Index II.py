class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        n = len(citations)
        
        for i in range(len(citations)):
            ans = max(ans, min(n - i, citations[i]))
        
        return ans
