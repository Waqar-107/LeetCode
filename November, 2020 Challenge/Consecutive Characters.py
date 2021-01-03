class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        n = len(s)
        
        i = 0
        while i < n:
            cnt = 1
            j = i + 1
            
            while j < n:
                if s[i] == s[j]:
                    cnt += 1
                    j += 1
                else:
                    break
            
            i = j
            ans = max(ans, cnt)
        
        return ans
