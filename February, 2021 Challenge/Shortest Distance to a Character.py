class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [math.inf] * n
        
        ch_idx = math.inf
        for i in range(n):
            if s[i] == c:
                ch_idx = i
            
            if ch_idx != math.inf:
                ans[i] = i - ch_idx
        
        ch_idx = math.inf
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                ch_idx = i
            
            ans[i] = min(ans[i], ch_idx - i)
        
        return ans
