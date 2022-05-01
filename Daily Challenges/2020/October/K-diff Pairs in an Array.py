class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        
        ans = 0
        if k == 0:
            for key in mp:
                if mp[key] > 1:
                    ans += 1
                    
            return ans
        
        
        for key in mp:
            if key + k in mp:
                ans += 1
        
        return ans
