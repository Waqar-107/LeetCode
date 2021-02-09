class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        
        for n in nums:
            cnt[n] += 1
        
        ans = 0
        for key in cnt:
            if cnt[key] == 1:
                ans += key
        
        return ans
