class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        th = n // 3 + 1
        
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        
        ans = set()
        for n in nums:
            if cnt[n] >= th:
                ans.add(n)
        
        return ans
