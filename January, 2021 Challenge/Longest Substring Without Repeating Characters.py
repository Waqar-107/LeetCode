class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        ans = 1
        i = 0
        j = 0
        cnt = defaultdict(int)
        cnt[s[0]] = 1
        
        while i < n and j < n:
            if i == j:
                j += 1
            
            elif cnt[s[j]] <= 0:
                ans = max(ans, j - i + 1)
                cnt[s[j]] += 1
                j += 1
            
            else:
                cnt[s[j]] += 1
                
                while i < j:
                    cnt[s[i]] -= 1
                    if cnt[s[i]] == 1:
                        i += 1
                        j += 1
                        break
                    
                    i += 1
                    
        return ans
                        
            
