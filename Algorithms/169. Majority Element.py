class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req = len(nums) // 2
        cnt = defaultdict(int)
        
        for n in nums:
            cnt[n] += 1
        
        for key in cnt:
            if cnt[key] > req:
                return key
