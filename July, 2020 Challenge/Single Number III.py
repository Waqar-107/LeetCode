class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        
        for num in nums:
            cnt[num] += 1
        
        ans = []
        for key in cnt:
            if cnt[key] == 1:
                ans.append(key)
        
        return ans
