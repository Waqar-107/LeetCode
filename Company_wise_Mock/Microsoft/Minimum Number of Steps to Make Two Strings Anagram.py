class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = defaultdict(int)
        for c in s:
            cnt_s[c] += 1
        
        cnt_t = defaultdict(int)
        for c in t:
            cnt_t[c] += 1
        
        ans = 0
        for key in cnt_t:
            print(key, cnt_s[key] - cnt_t[key])
            ans += max(0, cnt_t[key] - cnt_s[key])
        
        return ans
