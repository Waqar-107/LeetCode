class Solution:
    def solve(self, s, st, en, k):
        if en < k:
            return 0
        
        cnt = defaultdict(int)
        for i in range(st, en):
            cnt[s[i]] += 1
        
        for i in range(st, en):
            if cnt[s[i]] >= k:
                continue
            
            midNext = i + 1
            while midNext < en and cnt[s[midNext]] < k:
                midNext += 1
            
            return max(self.solve(s, st, i, k), self.solve(s, midNext, en, k))
            
        return en - st
        
    def longestSubstring(self, s: str, k: int) -> int:
        return self.solve(s, 0, len(s), k)
