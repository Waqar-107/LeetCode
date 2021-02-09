class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = []
        mod = int(1e9 + 7)
        
        p = 1
        for i in range(41):
            powers.append(p)
            p *= 2
        
        cnt = defaultdict(int)
        for e in deliciousness:
            cnt[e] += 1
        
        ans = 0
        for key in cnt:
            for p in powers:
                if abs(p - key) >= key and abs(p - key) in cnt:
                    if abs(p - key) == key:
                        x = (cnt[key] * (cnt[key] - 1)) // 2
                    else:
                        x = cnt[key] * cnt[abs(p - key)]
                    
                    ans = ((ans % mod) + x % mod) % mod
        
        return ans
